x_in = [0,1,2]
y_in = [1,2,4]

x= 1.5
y= 0

for i in range(len(x_in)):
    l=1
    for j in range(len(x_in)):
            if(i!=j):
                l =  l*((x-x_in[j])/(x_in[i]-x_in[j]))
    y += l*y_in[i]

print("the value calculated by interpolation is ",y)

def g(x):
    return 2**x

print("the value calculated by actual function 2^x  is ",g(x))

print("the difference between the actual 2^x and value calculated is ", (y-g(x)))

