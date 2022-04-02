#include <Python.h>


static PyObject *methodFputs(PyObject *self, PyObject *args) {
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
