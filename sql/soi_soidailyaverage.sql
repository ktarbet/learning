create PROCEDURE "cbp"."Soi_DailyAverage"( 
@TableName  varchar(256),
@ColName  varchar(256),
@tmstp1 datetime,
@tmstp2 datetime,
@WaterYear bit =0 -- shift all dates to the year 2000 for water year graphs
)
WITH RECOMPILE 
AS
BEGIN
-- Calculates daily average for SCADA system site tables
 --Example #1   daily average.
--call cbp.Soi_DailyAverage( 'site34','uslev','2002-07-01','2002-11-30')
--Example #2   daily average for water year graph/table
--call cbp.Soi_DailyAverage( 'site34','uslev','2002-07-01','2002-11-30',1)
declare @FullTableName varchar(128) -- owner.table
declare @qry varchar(512) -- dynamic sql query.
declare @qry2 varchar(512) -- dynamic sql query.
declare @SelectClause varchar(256)
declare @WhereClause varchar(256)
declare @tmstp datetime
declare @date1 datetime -- one day before we start our average.
declare @date2 datetime -- one day after we start our average.
declare @dateInterp datetime
declare @prevDate datetime
declare @DateIndex integer -- 0,1,2,....
declare @PrevDateIndex integer 
declare @value float(53)
declare @runningTotal float(53)
declare @prevValue float(53)
declare @valueInterp float(53)
declare @interpValue float(53) -- interpolated value at midnight
declare @incValue float(53) -- incremental value.

set @tmstp1 = convert(datetime,convert(varchar,@tmstp1,101))
set @tmstp2 = convert(datetime,convert(varchar,@tmstp2,101))
set @date1 = dateAdd(hour,-12,@tmstp1)
set @date2 = dateAdd(hour,36,@tmstp2)

set @SelectClause = 'SELECT tmstp, '+@ColName
set @WhereClause = ' where tmstp >= ''' + 
        Convert(varchar,@date1,120) + '''' 
        + ' and tmstp <= ''' + 
        Convert(varchar,@date2,120) + ''' and '
        +@ColName + ' is not null '
-- check if we need to use the arc table"?"
if year(@tmstp1) = year(current date)
    begin
    set @qry =@SelectClause + ' From cbp.'+@TableName+@WhereClause
        + ' order by 1 asc'
    end
else -- get union of archive data also.
   begin
        set @qry = @SelectClause +' from arc.'+@TableName+@WhereClause
               +' UNION '
               +  @SelectClause +' from cbp.'+@TableName+@WhereClause
               + ' order by 1'
   end

print @qry

-- create temp table for daily averages.
set @qry2 ='create table #AvgTable (tmstp datetime, '
      ||@ColName||' double)' --, note varchar(20))''
execute(@qry2)
--create table #AvgTable (tmstp datetime, value double, note varchar(20))
--set @counter =0
 begin
   print @qry
   declare crsr NO SCROLL CURSOR using @qry
   open crsr
    -- scan ahead until we find first date (skip leading dates)
   fetch next crsr into @tmstp, @value
   while (@@sqlstatus = 0 and @tmstp <@tmstp1) 
   begin
     set @prevDate = @tmstp
     set @prevValue = @value
     fetch NEXT crsr into @tmstp, @value
   end

    set @PrevDateIndex = datediff(day,@tmstp1,@prevDate)
    set @DateIndex = datediff(day,@tmstp1,@tmstp)     
    set @RunningTotal = 0
   while( @tmstp <@date2  and @@sqlstatus = 0)
    begin
    --print 'previous date --'
    --print Convert(varchar,@prevDate,120)+'-> '+Convert(varchar,@prevValue)
    if @PrevDateIndex = @DateIndex 
     begin -- For performance put most common if statment first.
       set @incValue =  DateDiff(second,@prevDate,@tmstp)
            * (@prevValue + @Value)* 0.005
       set @RunningTotal = @RunningTotal + @incValue
       -- insert into #AvgTable 
         --       values (@tmstp,@RunningTotal,'running total')
       end
       else --if @PrevDateIndex <> @DateIndex
     begin 
            -- if we are missing a day insert null.
        -- interpolate a midnight value.
      
       set @interpValue = cbp.Soi_Interpolate( 
           Date(@tmstp),@prevDate,@tmstp,@prevValue,@Value)
        -- portion before midnight belongs in previous days average.
        set @incValue = DateDiff(second,@prevDate,date(@tmstp))
                     * (@interpValue+@PrevValue)* 0.005
        set @RunningTotal = @RunningTotal + @incValue
        insert into #AvgTable 
                values (DateAdd(hour,12,date(@prevDate)),@RunningTotal/864)--,'Avg')
        -- portion after midnight it belongs in next days average
        set @incValue = DateDiff(second,date(@tmstp),@tmstp)
                     * (@interpValue+@value)*.005
        -- zero out running total
       set @RunningTotal =  @incValue
     end
        -- read next data point 
     set @prevDate = @tmstp
     set @prevValue = @value
     set @PrevDateIndex = @DateIndex
     fetch NEXT crsr into @tmstp, @value
       set @DateIndex = datediff(day,@tmstp1,@tmstp)     
    end
    close crsr

delete from #AvgTable where tmstp <@tmstp1 -- cleanup 

if @WaterYear =1
   begin -- shift all dates to year 2000 for water year graphs/tables.
  update #AvgTable set tmstp =  
     DateTime('2000'+'-'
        +trim(str(month(tmstp),2))
    +'-'+trim(str(day(tmstp),2)) 
    +' '+trim(str(hour(tmstp),2))+':'+trim(str(minute(tmstp),2))
    +':'+trim(str(second(tmstp),2))) 
         where tmstp is not null
   end
   select * from #AvgTable order by tmstp
 end
END
