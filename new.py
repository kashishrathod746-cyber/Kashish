#whether you will pass or fail

#print(2 > 2)

# marks = 50

# if marks >= 49.9:
#     print("you are passed")
# else:
    # print("you are failed")

#1.check number positive nagetive and zero

num=int(input("enter num:"))

if(num > 0):
    print("num is positive")

elif(num < 0):
    print("num is negative")
    
else:
    print("num is zero")



# 2.check if the number is even or odd


num=int(input("enter num:"))

if(num%2==0):
    print("num is even")
else:
    print("num is odd")


#3.find the greater of two num

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

if (num1 > num2):
    print("num1 is greater")
else:
    print("num2 is greater")


#4.three no comparion

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if (num1 >= num2 and num1 >= num3):
    print("num1 is greater")
elif(num2 >= num1 and num2 >= num3):
    print("num2 is greater")
else:
    print("num3 is greater")



#5.person is eligible for vote or not


age=int(input("enter age:"))
if(age>=18):
    print("you are eligible")
else:
    print("you are not eligible")  


# 6.leap year

year = int(input("Enter the year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#7.vowel and consonant
letter=input("Enter the letter: ")

if letter == "a" :
    print("vowel")
elif letter == "e" :
    print("vowel")
elif letter == "i" :
    print("vowel")
elif letter == "o" :
    print("vowel")
elif letter == "u" :
    print("vowel")
else:
    print("consonant")


#8.divisible by 5 and 11

num=int(input("enter num:"))

if (num % 5 == 0 and num % 11 == 0):
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")

#9.grade program

marks=int(input("enter your marks:"))

if marks >= 90 and marks <= 100:
    print("you got A grade")
elif marks >= 80 and marks < 89: 
    print("you got B grade")
elif marks >= 70 and marks < 70:
    print("you got C grade")
elif marks >= 60 and marks < 69:
    print("you got D grade")
else:
    print ("failed")


#10.Check if a character is uppercase or lowercase.

letter = input("Enter a character: ")

if letter.upper():
    print("Uppercase")
elif letter.lower():
    print("Lowercase")
else:
    print("Not a letter")


#11.Find whether the entered alphabet is a vowel using if-elif.

letter=input("Enter the letter: ")

if letter == "a" :
    print("vowel")
elif letter == "e" :
    print("vowel")
elif letter == "i" :
    print("vowel")
elif letter == "o" :
    print("vowel")
elif letter == "u" :
    print("vowel")
else:
    print("not vowel")


#12.Check if three sides can form a triangle.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Yes, these sides can form a triangle")
else:
    print("No, these sides cannot form a triangle")


#13.Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
        print("Equilateral Triangle")
elif a == b or b == c or a == c:
        print("Isosceles Triangle")
elif( a != b or b != c or a != b):
        print("Scalene Triangle")
        
else:
    print("Not a valid triangle")


#14.Find the largest among four numbers.


num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
num4=int(input("enter num4:"))
if (num1 > num2 and num1 > num3 and num1 > num4):
    print("num1 is greater")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("num2 is greater")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("num3 is greater")
elif(num4 >num1 and num4 > num2 and num4 >num3):
    print("num4 is greater")
else:
    print("same")


#15.Check whether a number is a three-digit number.


num=int(input("enter num:"))

if(num >= 100):
    print("the num is three digit")
else:
    print("the num is not three digit")

#17.Calculate electricity bill using slab rates.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
else:
    bill = units * 4

print("Electricity Bill =", bill)



#18.Calculate income tax based on income slabs.

income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 250000 * 0.05 + (income - 500000) * 0.2
else:
    tax = 250000 * 0.05 + 500000 * 0.2 + (income - 1000000) * 0.3

print("Income Tax =", tax)


#19Check if a student passes (minimum 35 marks in each subject).

sub=input("enter sub name:")
marks=int(input("enter sub marks:"))

if (marks >= 35):
    print("passed")
else:
    print("not passed")


#20.Find whether a number is within a given range


num = int(input("Enter a number: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

if num >= start and num <= end:
    print("The number is within the given range.")
else:
    print("The number is outside the given range.")



#21Build a simple calculator using if-elif-else (+, -, *, /).

a=int(input("enter a:"))
b=int(input("enter b:"))
operation=input("enter operator + - * / : ")



if operation == '+':
    print("Answer =", a + b)

elif operation == '-':
    print("Answer =", a - b)

elif operation == '*':
    print("Answer =", a * b)

elif operation == '/':
    print("Answer =", a / b)

else:
    print("not valid")


#22. Check if a year is a century leap year.

year = int(input("Enter the year: "))

if year % 400 == 0 :
    print("Century Leap Year")
else:
    print("Not a Leap Year")


#23.Determine the season based on the month number.

month=input("enter month november,december,january,februay,march,aprill,,may,june,july ,august ,september,october:")


if (month in "november,december,january,februay"):
    print("winter")

elif(month in "march,aprill,,may,june"):
    print("summer")

elif (month in "july ,august ,september,october"):
    print("rainy")

else:
    print("not valid")



#24.Find the number of days in a month.


month=input("enter month november,december,january,februay,march,aprill,,may,june,july ,august ,september,october:")


if (month in "january,march,may,july august,october,december"):
    print("31 days")

elif(month in "aprill,june,september,november"):
    print("30 days")

elif (month in "february"):
    print("28 and 29 days")

else:
    print("not valid")
    


#25.Check whether a password meets minimum conditions (length, digits, etc.)

password = input("Enter your password: ")

if len(password) >= 8:
    print("Password is Strong")
else:
    print("Password is Weak")

#26.Determine ticket price based on age category.

age = int(input("Enter your age: "))

if age < 5:
    print("Ticket Price = Free")
elif age <= 12:
    print("Ticket Price = 100")
elif age < 60:
    print("Ticket Price = 200")
else:
    print("Ticket Price = 150")


#27.Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Discount =", discount)
print("Final Amount =", final_amount)


#28.Check if a person is eligible for a driving license (age and eyesight condition).

age=int(input("enter age:"))
eyesight = input("Is your eyesight good? (yes/no): ")
if(age>=18 and eyesight == "yes"):
    print("you can drive")
else:
    print("you cannot drive")



#29.Create a login system with username and password validation

username= input("Enter username:")
password= input("Enter password:")

if username == "admin" and password == "1234":

    print("Login successfully")
else:
    print("Enter your password:")


#30.Create a menu-driven program using if-elif-else with options like:
# Addition
# Subtraction
# Multiplication
# Division
# Exit


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)

elif choice == 5:
    print("Exit")

else:
    print("Invalid Choice")