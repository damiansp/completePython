#define PY_SSIZE_T_CLEAN
#include <Python.h>


long long fibonacci(unsigned int n) {
  if (n == 0 || n == 1) {
    return n;
  }
  return fibonacci(n - 2) + fibonacci(n - 1);
}


static PyObject* fibonacci_py(PyObject* self, PyObject* args) {
  PyObject* result = NULL;
  long n;
  long long fib;

  if (PyArg_ParseTuple(args, "l", &n)) {
    if (n < 0) {
      PyErr_SetString(PyExc_ValueError, "n cannot be < 0");
    } else {
      Py_BEGIN_ALLOW_THREADS;
      fib = fibonacci(n);
      Py_END_ALLOW_THREADS;
      result = Py_BuildValue("L", fib);
    }
  }
  return result;
}


static char fibonacci_docs[] = (
  "fibonacci(n): Return nth Fibonacci sequence number computed recursively\n");
static PyMethodDef fibonacci_module_methods[] = {
  {"fibonacci", (PyCFunction) fibonacci_py, METH_VARARGS, fibonacci_docs},
  {NULL, NULL, 0, NULL}};


static struct PyModuleDef fibonacci_module_definition = {
  PyModuleDef_HEAD_INIT,
  "fibonacci",
  "Extension module that provides fibonacci sequence function",
  -1,
  fibonacci_module_methods};


PyMODINIT_FUNC PyInit_fibonacci(void) {
  Py_Initialize();
  return PyModule_Create(&fibonacci_module_definition);
}
