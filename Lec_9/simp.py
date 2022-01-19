import numpy as np;
def f(x):
    return 10 - 3*(x**2);

b = 3;
a = -1;
n = np.linspace(a,b,4)
inf = (b-a)/(3*4);
Sum = 0;
for i in range(a,b,4):
    Sum += inf*(f(n[i])+f(n[i+1]) +4*f((n[i]+n[i+1])/2))*2;
print("the integral is ",Sum)
