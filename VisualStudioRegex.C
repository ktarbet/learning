
```C
#define DSS_END_HEADER_FLAG		-97531
internal const int DSS_START_CAT_SORT_FLAG = -97536;
```

```
find
#define\s+(\w+)\s+([0-9-+]+)
replace:
internal const int $1 = $2;
```
