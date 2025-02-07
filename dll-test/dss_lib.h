#ifndef DSS_LIB_H
#define DSS_LIB_H


#ifdef __cplusplus
extern "C" {
#endif


#ifdef _WIN32
  #ifdef DSS_LIB_EXPORTS
    #define DSS_API __declspec(dllexport)  // Exporting symbols
  #else
    #define DSS_API __declspec(dllimport)  // Importing symbols
  #endif
#else
  #define DSS_API  // No special attributes for non-Windows
#endif

DSS_API int compute_value(int input);

#ifdef __cplusplus
}
#endif

#endif // DSS_LIB_H
