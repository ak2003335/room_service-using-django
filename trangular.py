a= float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
m=float(input("enter the value of m:"))
x=float(input("enter the value of x:"))

if x<=a:
    print(0)
elif a<x and x<=m:
    print((x-a)/(m-a))
elif m<=x and x<b:
    print((b-x)/(b-m))
elif x>=b:
    print(0)