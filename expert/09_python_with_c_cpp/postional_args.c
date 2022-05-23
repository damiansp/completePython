#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject8 print_args(PyObject* self, PyObject* args, PyObject*, keywds) {
  char* first;
  char* second;
  static char* kwlist[] = {"first", "second", NULL};

  if (!PyArg_ParseTupleAndKeywords(args, keywds, "ss", kwlist, &first, &second))
    {
      return NULL;
  }
  printf("%s %s\n", first, second);
  Py_INCREF(Py_None);
  return Py_None
}


static PyMethodDef module_methods[] = {
  {"print_args",
   (PyCFunction) print_args,
   METH_VARARGS | METH_KEYWORDS,
   "print provided arguments"},
  {NULL, NULL, 0, NULL}};


static struct PyModuleDef module_definition = {
  PyModuleDef_HEAD_INIT,
  "kwargs",
  "Keyword argument processing example",
  -1,
  module_methods
};


PyMODINIT_FUNC PyInit_kwargs(void) {
  return PyModule_Create(&module_definition);
}
