CFLAGS=$(python-config --cflags)
LDFLAAGS=$(python-config --ldflags)
cython fib.pyx                          # --> outputs fib.c
gcc -c fib.c ${CFLAGS}                  # --> outputs fib.o
gcc fib.o -o fib.so -shared ${LDFLAGS}  # --> outputs fib.so
