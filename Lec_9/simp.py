def f(x):
    return 10 - 3*(x**2);

b = 3
a = -1
n = 4
inf = (b-a)/n
Sum = 0;
for i in range(1,n):
    if i%2 == 1:
        Sum += 4*f(a + inf*i)
    else:
        Sum += 2*f(a + inf*i)

Sum += f(a) + f(b)
Sum = Sum*(b-a)/(3*n)
print("the integral is ",Sum)
