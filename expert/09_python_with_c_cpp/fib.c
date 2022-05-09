#include <stdio.h>


long long fibonacci(unsigned int n) {
  if (n == 0 || n == 1) {
    return n;
  }
  return fibonacci(n - 2) + fibonacci(n - 1);
}


int main() {
  int n = 26;
  long long fibn = fibonacci(n);
  printf("fin(26): %lld\n", fibn);
  return 0;
}
