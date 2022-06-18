double cfib(int n) {
  int i,
    temp,
    a = 1,
    b = 0;
  for (i = 0; i < n; ++i) {
    temp = a;
    a = a + b;
    b = temp;
  }
  return a;
}
