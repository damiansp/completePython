cdef extern from 'string.h':
    char* strstr(const char *haystack, const char *needle)


cdef char* data = 'oiabujagait a[hunj[,i,f,0awfmhuaoijoafbipai'
cdef char* pos = strstr(needle='awf', haystack=data)
print(pos is not NULL)
