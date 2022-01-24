a1 = 0
a2 = 1
a3 = 2
fa1 = 1
fa2 = 2
fa3 = 4
def f(x):
    return (((x-a2)*(x-a3))/((a1-a2)*(a1-a3)))*fa1 + (((x-a1)*(x-a3))/((a2-a1)*(a2-a3)))*fa2 + (((x-a1)*(x-a2))/((a3-a1)*(a3-a2)))*fa3

print("the value calculated by interpolation is ",f(1.5))

def g(x):
    return 2**x

print("the value calculated by actual function 2^x  is ",g(1.5))

print("the difference between the actual 2^x and value calculated is ", (f(1.5)-g(1.5)))

