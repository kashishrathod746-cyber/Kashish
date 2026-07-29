#Taking input from user & printing it
name = input ("name :")
age = input("age :")
price = float(input("price :"))
print("My name is",name,"and I am",age,"years old")


#Trafic light code
#Conditional statement
light = input("Light :")
if (light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look") 
else:
    print("light is broken")   


#Grades of student
marks = int(input("marks :"))
if(marks >= 90):
    print("A")
elif(marks >=80 and marks < 90):
    print("B")
elif(marks <= 70 and marks < 80 ):
    print("C")
else:
    print("D")

#Practice Time
A = int(input("A : "))
G = input("M/F :")
if((A == 1 or A == 2) and G == "M"):
   print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")


    