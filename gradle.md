#  Gradle

## 

```  
init  : determine what project(s) to build    init.gradle ,  *.gradle, settings.gradle
        .gradle/init.d/a.gradle
        .gradle/init.d/b.gradle
        .gradle/init.d/z.gradle

settings.gradle 

config  :  build.gradle
exec : build.gradle  (tasks)
```

##  Script  API

myfile.gradle   (uses Script API)
  
  -i for logging
  
  logger.info "info level message"

```
  apply {
    println "hi from clousure code"
  }
```  
