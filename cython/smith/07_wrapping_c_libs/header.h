#define M_PI 3.1415926
#define MAX(a, b) ((a) >= (b) ? (a) : (b))


typedef int integral;
typedef double real;

double hypot(double, double);
void func(integral, integral, real);
real *func_arrays(integral[], integral[][10], real **);
