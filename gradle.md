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


## Gradle Objects
# Gradle Build Phases and Delegate Objects

| Phase | Script File | Delegate Object | Description | Common Operations |
|-------|-------------|-----------------|-------------|-------------------|
| **Initialization** | `settings.gradle(.kts)` | `Settings` | Determines which projects participate in the build | `include()`, `pluginManagement {}`, `rootProject.name` |
| **Configuration** | `build.gradle(.kts)` | `Project` | Configures the project object model (tasks, dependencies, etc.) | `dependencies {}`, `repositories {}`, `plugins {}`, task registration |
| **Execution** | N/A (task actions) | `Task` | Executes the task action code | `doFirst {}`, `doLast {}`, actual build work |


https://docs.gradle.org/current/dsl/org.gradle.api.initialization.Settings.html
https://docs.gradle.org/current/dsl/org.gradle.api.Project.html
https://docs.gradle.org/current/dsl/org.gradle.api.Task.html


##  build.gradle example methods

| example |what's this/ ref? |
| --- |---|
| logger.info "abc ${project.gradle.timestamp()} "  |  |
| project.gradle.gradleVersion | https://docs.gradle.org/current/dsl/org.gradle.api.invocation.Gradle.html#content |
| project.gradle.gradleHomeDir | |
| project.gradle.gradleUserHomeDir |  |

##  Script  API

myfile.gradle   (uses Script API)
  
  -i for logging
  -Pkey1=value1
  
  logger.info "info level message"

```
  apply {
    println "hi from clousure code"
```


## gradle.properties 

name=value
name2=value2

can add properties onto existing built-in objects.

project.gradle.hasProoperty('gradleVersion')

in build.gradle can use shortcut:
hasProoperty('gradleVersion')


project.ext.myprop ="Snake River"

if (project.hasProperty('myprop') ) {
    logger.info myprop
  } else {
  logger.info "can't find myprop"
  }









  }
```


## Project Plugins

 - Core https://docs.gradle.org/current/userguide/plugin_reference.html#header  ( don't need to specify version)
 - Community  https://plugins.gradle.org/
 - Local Plugin  implemented locally


* plugins give provide new tasks
* add new confiugrations
* initilize configuration


### More on  core plugins

java - SourceSet  (default src/main/java,  src/test/java)
java-library (includes java) -- api configuration is added
application (includes java) -  specifiy main, and run task



