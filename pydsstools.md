How to get pydss tools installed and working/development setup

# LINUX

pip3 install --user pandas
pip3 install --user NumPy
pip3 install --user affine
pip3 install --user Cython
pip3 install --user config

sudo yum install gdal
pip3 install --user  GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}') --global-option=build_ext --global-option="-I/usr/include/gdal"




# WINDOWS 


http://winpython.github.io/

Download/unzip Winpython64-3.7.7.0.exe  (or newer) into c:\programs\

Add this to path:  (or hopefully something cleaner, I just unzipped)

C:\Programs\winpython64-3.7.7.0\WPy64-3770\python-3.7.7.amd64

Clone the repository (might also work to just copy) to c:\project\pydss

https://github.com/gyanz/pydsstools


Open command prompt:

C:\project\pydss\pydsstools>python setup.py build

C:\project\pydss\pydsstools>python setup.py install

cd pydsstools\examples

C:\project\pydss\pydsstools\pydsstools\examples>python example1.py
11:17:01.711      -----DSS---zopen   Existing file opened,  File: C:\project\pydss\pydsstools\pydsstools\examples\example.dss
11:17:01.713                         Handle 3;  Process: 18748;  DSS Versions - Software: 7-HS, File:  7-HL
11:17:01.717                         Single-user advisory access mode
11:17:01.718 -----DSS--- zdelete  Handle 3;  Pathname: /REGULAR/TIMESERIES/FLOW/01Jul2019/1Hour/Ex1/
11:17:01.724 -----DSS--- zwrite  Handle 3;  Version 1:  /REGULAR/TIMESERIES/FLOW/01Jul2019/1Hour/Ex1/
11:17:01.731 -----DSS--- zread   Handle 3;  Version 1:  /REGULAR/TIMESERIES/FLOW/01Jul2019/1Hour/Ex1/
11:17:01.733      -----DSS---zclose  Handle 3;  Process: 18748;  File: C:\project\pydss\pydsstools\pydsstools\examples\example.dss
11:17:01.738                         Number records:         4
11:17:01.739                         File size:              9700  64-bit words
11:17:01.743                         File size:              75 Kb;  0 Mb
11:17:01.745                         Dead space:             887
11:17:01.748                         Hash range:             4096
11:17:01.751                         Number hash used:       13
11:17:01.751                         Max paths for hash:     1
11:17:01.752                         Corresponding hash:     3976
11:17:01.755                         Number non unique hash: 0
11:17:01.764                         Number bins used:       13
11:17:01.764                         Number overflow bins:   0
11:17:01.765                         Number physical reads:  60
11:17:01.765                         Number physical writes: 12
11:17:01.768                         Number denied locks:    0

