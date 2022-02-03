

## build class path

CLASSPATH=$(find ~/.m2/repository -name '*.jar' | xargs echo | tr ' ' ':')
CLASSPATH=${CLASSPATH}:.:../hec-monolith-0.0.4-SNAPSHOT.jar

======================
#!/bin/bash
#KARL=$(find ~/.m2/repository -name '*.jar' | xargs echo | tr ' ' ':')

R=/home/usace/q0hecklt/.m2/repository/
A=${R}com/google/flogger/flogger/0.3.1/flogger-0.3.1.jar
A=${A}:${R}com/google/flogger/flogger-system-backend/0.3.1/flogger-system-backend-0.3.1.jar
A=${A}:${R}org/junit/jupiter/junit-jupiter-api/5.7.0/junit-jupiter-api-5.7.0.jar
A=${A}:${R}org/junit/platform/junit-platform-commons/1.7.0/junit-platform-commons-1.7.0.jar
A=${A}:${R}mil/army/usace/hec/hec-nucleus-metadata/1.0.28/hec-nucleus-metadata-1.0.28.jar
A=${A}:${R}org/opentest4j/opentest4j/1.2.0/opentest4j-1.2.0.jar
A=${A}:../hec-monolith-0.0.4-SNAPSHOT.jar
${A}:.

#echo $H

java -cp ${A}:. -Djava.library.path=../../../hec-dss/heclib/javaHeclib/Output  hec.heclib.grid.GridTest
