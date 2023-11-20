
## Time Series

Queries from Dave P.

Count all rows of data

```
select sum(num_rows) total_rows
from dba_tables 
where regexp_instr(table_name,'^AT_TSV_([0-9]){4}$')=1 or table_name = 'AT_TSV_ARCHIVAL'
order by table_name;
```


Storage allocation
```
select tablespace_name, 
       round(maxbytes/1024/1024,0) "Max Size (M)", 
       round(user_bytes/1024/1024,0) "Size (M)", 
       decode(maxbytes,0,0, round(user_bytes*100/maxbytes,0)) "% of Max" 
from   dba_data_files 
where  tablespace_name='CWMS_20_TSV'
order  by 1,user_blocks desc;

```

Used Bytes

```
select used_bytes/1024/1024 "Used Bytes (M)"
from   dba_data_files df left join 
       ( select file_id, sum(bytes) used_bytes
         from   dba_extents
         group  by file_id
       ) e
       on (df.file_id = e.file_id )
WHERE  df.tablespace_name='CWMS_20_TSV';

```



## Ratings


Java Ratings  (hec.data.cwmsRating)    RatingSet.java  many constructors. 

Oracle Ratings (in cwms oracle )

RatingSet.databaseLoadMethod.[
EAGER (everthing),
LAZY (stubs no data until needed),
REFERENCE (enough info to let oracle do work )
]
 

## Rating Format

XML  (eager or Reference includes <rating-points>)

RADAR  more efficient rating points in more unformated/raw/minimize-whitespace
 
  
  
```sql 
 (SELECT cwms_ts_id,
       data_entry_date,
       VALUE,
       quality_code
  FROM av_tsv v, at_cwms_ts_id d
 WHERE     v.ts_code = d.ts_code
       AND (   cwms_ts_id LIKE 'STJ%Flow%1Hour%Best-NWDM'
            OR cwms_ts_id LIKE 'MKC%Flow%1Hour%Best-NWDM'
            OR cwms_ts_id LIKE 'HEMO%Flow%1Hour%Best-NWDM')
       AND quality_code=5
       AND date_time > SYSDATE - 1)


```






