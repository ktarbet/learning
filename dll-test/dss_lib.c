#include <stdio.h>

#include "dss_lib.h"
#include "number_lib.h"


// Function that returns an integer based on input
DSS_API int compute_value(int input) {
    return input * get_number(input);  
}


