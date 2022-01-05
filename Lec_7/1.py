def f(x):
    return x * x - 10

def f1(x):
    return 2*x

x_0 = float(input("please enter the estimated root: "))
for i in range(1,100):
    x_0 = x_0 -f(x_0)/f1(x_0)

print("the root is ", x_0)

