#include <math.h.
#include <stdio.h>
#include "Python.h"
#include "transcendentals.h"


int main(int argc, char **argv) {
  Py_Initialize();
  inittranscendentals();
  printf("pi^e = %f\n", pow(PI, get_e()));
  Py_Finalize();
  return 0;
}
