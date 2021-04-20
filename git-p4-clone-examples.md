!/bin/bash

#!/bin/bash
source /home/karl/.bash_profile
export P4PORT=perforce-server:1666

rm -fr ./hec-dssvue-v30
git init hec-dssvue-v30
cd hec-dssvue-v30

P=-//DSSVue/DSSVue/v3.0
export IGNORE30="${P}/apps/ ${P}/dist/ ${P}/lib/ ${P}/obfuscate/ ${P}/install/"

git p4 clone -v --destination=.  //DSSVue/DSSVue/v3.0@all ${IGNORE30} | tee ../create-dssvue-v30.log 


=================================================================
=================================================================
P=-//heclib
export IGNORE="${P}/archive/ ${P}/develop/ ${P}/lib/ ${P}/Intel/ ${P}heclib7/headers/Java/"

git init heclib-archive
cd heclib-archive

git p4 clone -v --destination=. //heclib@all ${IGNORE} | tee ../create-rma-heclib.log

# 
