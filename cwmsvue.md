

#debuging

add the following to CWMS-Vue.config (other path optional)

```bash
vmparam -Djava.util.logging.config.file=c:/tmp/logging.properties
```

inside logging.propertiese  (start with copy from somewhere)
add this line

```bash
usace.cwms.db.jooq.dao.CwmsDbTsJooq.level=FINEST
```
