#ifndef NUMBER_LIB_H
#define NUMBER_LIB_H

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

DLL_EXPORT int get_number(int input);

#endif // NUMBER_LIB_H
