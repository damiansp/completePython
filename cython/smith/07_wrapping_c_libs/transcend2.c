#include <stdio.h>
#include "transcend2_api.h"


int main(int argc, char **argv) {
  import_transend2();
  printf("e: %f\n", get_e());
  return 0;
}
