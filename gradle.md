#  Gradle

## 
  
init  : determine what project(s) to build    init.gradle , settings.gradle
config  :  build.gradle
exec : build.gradle  (tasks)


##  Script  API

myfile.gradle   (uses Script API)
  -i for logging
  logger.info "info level message"

  apply {
    println "hi from clousure code"
  }
  
