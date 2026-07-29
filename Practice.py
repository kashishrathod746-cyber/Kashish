# find square of a number
num = int(input("Enter a number:"))
square = num * num
print("Square =",square)

#celsius to fahrenheit
c = float(input("Enter temperature in celsius:"))
f = (c*9/5)+34
print("Temperature =",f)

#swap two numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
a,b = b,a
print("After swap:")
print("a =",a)
print("b =",b)

#area of rectangle
length = float(input("Enter length:"))
width = float(input("Enter width:"))
area = length * width
print("Area =",area)

#simple interest
p = float(input("Principal:"))
r = float(input("Rate:"))
t = float(input("Time:"))
si = (p * r * t) / 100
print("simple interest =",si)

#area of circle