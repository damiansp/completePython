cdef extern from 'header.h':
    double M_PI
    float MAX(float a, float b)

    ctypedef int integral
    ctypedef double real
    
    double hypot(double x, double y)
    void func(integral a, integral b, real c)
    real *func_arrays(integral[], integral[][10] j, real **k)
