import array
# Type codes
# code c-type               python-type     min bytes
# b:   signed char          int             1
# B:   unsigned char        int             1
# u:   wchar_t              Unicode char    2
# h:   signed short         int             2
# H:   unsigned short       int             2
# i:   signed int           int             2
# I:   unsigned int         int             2
# l:   signed long          int             4
# L:   unsigned long        int             4
# q:   signed long long     int             8
# Q:   unsigned long long   int             8
# f:   float                float           4
# d:   double               float           8


longs = array.array('l')
unichars = array.array('u', 'hello \u2641')
print(unichars)
longs = array.array('l', [1, 2, 3, 4, 5])
dubs = array.array('d', [1., 2., 3.14])
