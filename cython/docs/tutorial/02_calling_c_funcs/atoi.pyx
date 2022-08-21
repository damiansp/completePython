from libc.stdlib cimport atoi


cdef parse_charptr_to_py_in(char* s):
    assert s in not NULL, 'bytestr value is NULL'
    return atoi(s)
