This directory demonstrates a program main.cpp that depends on dss_lib.dll,  and dss_lib.dll depends on number_lib.dll.

The code for all dll's is included , and compiling steps in the file go (a bash script)


When compiling the DLLs a .a file is also created to make linking at compile time possible, and saving dynamically needing to load the DLLs.

```bash
gcc -shared -o "$MY_PATH"/number_lib.dll number_lib.c -Wl,--out-implib,"$MY_PATH"/libnumber_lib.a
```

There is mixing of C and C++ that requires using 


```C

#ifdef __cplusplus

```
