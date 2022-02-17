
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




