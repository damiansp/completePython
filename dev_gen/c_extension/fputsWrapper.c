#include <Python.h>


static PyObject *method_fputs(PyObject *self, PyObject *args) {
  char *str, *filename = NULL;
  int bytesCopied = -1;

  /* Parse args */
  if (!PyArg_ParsTuple(args, "ss", &str, &filename)) {
    return NULL;
  }

  FILE *fp = fopen(filename, "w");
  bytesCopies = fputs(str, fp);
  fclose(fp);
  return PyLong_FromLong(bytes_copied);
}


static MyMethodDef FputsMethods[] = {
  {"fputs",
   method_fputs,
   METH_VARARGS,
   "Python interface for fputs C library function"},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fputsmodule = {
  PyModuleDef_HEAD_INIT,
  "fputs",
  "Python interface for fputs C library function",
  -1,
  FputsMethods
};


PyMODINIT_FUNC PyInit_fputs(void) {
  return PyModule_Create(&fputsmodule);
}
