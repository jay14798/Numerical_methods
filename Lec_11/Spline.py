from scipy.interpolate import CubicSpline
x = [0,1,2]
y = [1,2,4]
cs=CubicSpline(x,y)
n = 1.5
print("Using Spline interpolation we find :", cs(n))
print("the correct value is", 2**n)
