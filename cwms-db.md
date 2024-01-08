
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

 monitor CCP

```sql
SELECT count( * ) FROM ccp.cp_comp_tasklist;

-- If count > 50,000, we throw a “yellow” light.

SELECT machine,
       count( * ) "COUNT",
       ( sysdate - MIN( logon_time ) ) "LOGIN_DAYS",
       ( sysdate - MAX( prev_exec_start ) ) * 1440 "LAST_ACTIVITY_MINUTES"
  FROM v$session WHERE username = ‘G0DCSA26’
GROUP BY machine;

--  if count < 2, we throw a “red” light.  If the last activity returned is > 15 minutes, we throw a “yellow”, if > 60 a “red”.  The machine and login days are just displayed.

SELECT nvl( sysdate - MIN( date_time_loaded ), 0 ) age
 FROM ccp.cp_comp_tasklist''' )

-- If age > 2 days, we throw a “yellow” light, if > 5 a “red”.

SELECT ( last_tsv - last_ccp ) * 24 * 60 ccp_lag FROM
  ( SELECT ( SELECT CAST( MAX( data_entry_date ) AS date )
               FROM cwms_20.at_tsv_count )       last_tsv,
  ( SELECT CAST( MAX( data_entry_date ) AS date )
      FROM ccp.cp_comp_tasklist_count ) last_ccp
  FROM dual );

-- If ccp_lag is over 10 minutes, we throw a “yellow”, if over 30 a “red”


SELECT COUNT( DECODE( msg_state, 'READY',     1 ) ) ready,
       COUNT( DECODE( msg_state, 'PROCESSED', 1 ) ) processed
FROM   cwms_20.aq$nwdp_ts_stored_table
WHERE  consumer_name='CCP_SUBSCRIBER;

-- If ready is > 100, we throw a “yellow” light, if > 1000 a “red”

We also show a summary based on:

SELECT loading_application_name                 "CCP Process",
       TRUNC( ( sysdate - heartbeat ) * 86400 ) "Heartbeat (sec)",
       SUBSTR( cur_status, 7 )                  "Computations"
FROM   ccp.ref_loading_application_prop LEFT JOIN
       ccp.cp_comp_proc_lock USING ( loading_application_id ) LEFT JOIN
       ccp.hdb_loading_application USING ( loading_application_id )
WHERE  LOWER( prop_name ) = 'compproc_util' AND LOWER( prop_value ) = 'true'
ORDER BY 1;


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


## LRTS

```sql
SELECT db_office_id, COUNT(ts_code) num_ts_ids
FROM cwms_v_Ts_id
WHERE INSTR(cwms_Ts_id, '~') > 0
AND interval_utc_offset != -2147483648
GROUP BY db_office_id
```


