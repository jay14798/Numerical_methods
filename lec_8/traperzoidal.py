import numpy as np
n = int(input("Please enter number of intervals:"))
def f(x):
    return 10 - x**2;

inf = 4/n
A = ((f(-2) + f(2))/2)*inf
j = np.linspace(-2,2,n)
for i in range(1,n-1):
    A += inf * f(j[i])

print("the area calculated by trapizoidal rule is:", A)

