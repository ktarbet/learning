### Windows



https://gdal.org/en/stable/download.html#vcpkg

```bat
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh  # ./bootstrap-vcpkg.bat for Windows
./vcpkg integrate install
./vcpkg search gdal --featurepackages  # list optional features
./vcpkg install gdal[tools]  # get command line tools.

```


### Rocky Linux 8

```bash
sudo yum install curl-devel
sudo yum install qgis



sudo yum install sqlite-devel
sudo yum install libtiff-devel
sudo yum install libtiff-devel

```

# compile proj-8.2.1

```
./configure
make -j6
sudo make install

```
