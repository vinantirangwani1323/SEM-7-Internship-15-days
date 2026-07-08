



#Area of the rectangle
length = float(input("Enter the value of length:"))
breath = float(input("Enter the value of breath:"))
area = length * breath
print("The area of rectangle:", area)

#Area of the square
l = float(input("Enter the value of length:"))
areaofsquare = l*l
print("The area of square is:",areaofsquare)

#Area of circle
radius = float(input("Enter the value:"))
pi = 3.141592653589
areaofcircle = (pi*radius*radius)
print("The area of circle is:",areaofcircle)

#average of 5 numbers
n1 = int(input("Enter the value of n1:"))
n2 = int(input("Enter the value of n2:"))
n3 = int(input("Enter the value of n3:"))
n4 = int(input("Enter the value of n4:"))
n5 = int(input("Enter the value of n5:"))
average = ((n1 + n2 + n3 + n4 + n5)/5)
print("The average values of the 5 numbers entered:",average)

#calculate the simple interest
p = float(input("Enter the value of the principal amount:"))
r =  float(input("Enter the value of the rateof interest:"))
t = float(input("Enter the value of the tenure:"))
SI = ((p * r * t)/100)
print("The simple interest is:",SI)

#Find the cube and square of the entered 3 nos.

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

nums = [a, b, c]
for num in nums:
 squares = num**2
 cube = num**3
 print(f"{num}     |{squares}     |{cube}")

#Program to convert f to celsius
F = float(input("Enter the value in F:"))
C = [((F - 32)*5)/9]
print("The temperature in celsus is:",C)

#check whether the no. is even or odd
num1= int(input("Enter the number 1:"))
if num1 % 2==0:
 print("The number is even:")
else:
 print("The number is odd")

#leap year or not
year = int(input("Enter the year:"))
if year % 4==0:
 print("The year entered is leap year:", year)
else:
 print("The year entered is not leap year:",year)

#find the smallest number out of the 2

num2 = int(input("Enter the value of num2:"))
num3 = int(input("Enter the value of the num3:"))
if num2 < num3:
 print("Num2 is less than num3",num2)
else:
 print("Num3 is less",num3)

#wether num is postive, negative or zero
n = int(input("Enter the value of the number:"))

if n ==0:
 print("The number is zero",n)
elif n > 0:
 print("the number is postive:",n)
elif n < 0:
 print("The number is negative:",n)

#find the greatest num of 2
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of the y:"))
if x > y:
 print("x is greater than y",x)
else:
 print("y is greater",y)

#age where are you able to vote
age = int(input("Enter the age:"))
if age > 18:
 print("You are eligible to vote")
else:
 print("You are not eligible")
 
#a program to check whether the blood donor is eligible or not for donating blood. The conditions laid down are as under. Use if statement. • Age should be above 18 year but not more than 55 year. 
age = int(input("Enter the age:"))
if age > 18 and age <= 55:
 print("You are eligible to donate")
else:
 print("You are not eligible")

#if the number is greater than 10 then print square the of the number
c = int(input("ENter the number of your choice:"))
if c > 10:
 print("Thesquare number is :",c**2)
else:
 print("Sorry the number is not greater than 10")

#if the number is less than 100 then print whether the number is odd or even 
number = int(input("The number is :"))
if number < 100:
 if number / 2 == 0:
  print("The nujmber is even")
 else:
  print("The number is odd")
else:
 print("The number is greater than 100")

#find the largest number of the 3 without using conditional statements or logival statements
d = int(input("Enter the number:"))
e = int(input("Enter the number:"))
f = int(input("Enter the number:"))

maximumNo = max(d, e, f)
print("The maximum number is:",maximumNo)

#find using nested if else whether the number is 0, postive or negative
no1 = int(input("Enter the number:"))
if no1 > 0:
 print("The number is positive")
else:
 if no1 < 0:
  print("The number is negative")
 else: 
  print("The number is 0")

#find the greatest of the 3 numbers using nested if 
h = int(input("Enter the number:"))
i = int(input("Enter the number:"))
j = int(input("Enter the number:"))

if h > i and h > j:
 print("The h is the greatest ")
else:
 if  i > j and i > h:
  print("The i is greater")
 else:
  print("The j is greater")


#find the smallrest of the 3 numbers using logical operaators
k = int(input("Enter the number:"))
l = int(input("Enter the number:"))
m = int(input("Enter the number:"))

if k < l and k < m:
 print("The k is the smalltest ")
else:
 if  l < m and l < k:
  print("The l is smaller")
 else:
  print("The m is smaller")

#find the factorial of the number 
n = int(input("Enter the number:"))
fact = 1
for i in range(1 , n + 1):
 fact = fact * i
print("The factorial of the number is:",fact)

# Do the swap of the 2 variable using the third variable
p= int(input("Enter the value of p:"))
q = int(input("Enter the value of q:"))

temp = p
p = q
q = temp
print("The value after the swap of p:",p)
print("The value after the swap of q:",q)

#TAKE A NUMBER AND GENERATE THE MULTIPLICATION TABLE OF THAT NUMBER 
r = int(input("Enter the number of your choice for table:"))
for i in range(1, 11, 1):
 print(r, "*", i, "=", r*i)

#take a number and find the sum of the natural numbers
nm = int(input("Enter the number:"))
sum = 0
for i in range(1, nm + 1):
 sum = sum + i
print("The sum of numbers",nm, "is:",sum)

#Take a number. If the number is 1 then print Monday, 2 then tuesday and so on 
day = int(input("Enter the number:"))
match day:
 case 1:
  print("Monday")
 case 2:
  print("Tuesday")
 case 3:
  print("Wednesday")
 case 4:
  print("Thrusday")
 case 5:
  print("Frday")
 case 6:
  print("Saturday")
 case 7:
  print("Sunday")

#Take a number. If the number is 1 then print Jan, 2 then Feb and so on 
month = int(input("Enter the number:"))
match month:
 case 1:
  print("January")
 case 2:
  print("February")
 case 3:
  print("Maarch")
 case 4:
  print("April")
 case 5:
  print("May")
 case 6:
  print("June")
 case 7:
  print("July")
 case 8:
  print("August")
 case 9:
  print("September")
 case 10:
  print("October")
 case 11:
  print("November")
 case 12:
  print("December")
  
#Simple calculator using match case
s = int(input("Enter the value of the number:"))
t = int(input("Enter the vlaue of the number:"))
value = int(input("Enter the value:"))

match value:
 case 1:
  print("The sum is:", s + t)
 case 2:
  print("The sub is:", s - t)
 case 3:
  print("The mul is:", s * t)
 case 4:
  print("The div is", s / t)

#marks and grading of the students 
print("Marks of student 1 out of 100")
Maths = float(input("Enter marks of Maths :"))
Sci = float(input("Enter marks of Sci:"))
Social = float(input("Enter marks of Social:"))
Eng =  float(input("Enter marks of Eng:"))
Guj = float(input("Enter Guj:"))

Total = Maths + Sci + Social + Eng + Guj
print("Total marks",Total)
average = Total / 5
print("The average marks of the student:",average)
percentage = Total / 500 * 100
print("The percentage is:", percentage)

if average < 50:
 print("The Grade is F")
if average >= 50 and average < 60:
  print("The Grade is D")
if average >= 60 and average < 70:
   print("The Grade is C")
if average >= 70 and average < 80:
  print("The Grade is B")
if average >= 80 and average < 90:
  print("The Grade is A")
if average >= 90 and average <= 100:
  print("The Grade is A+")


  
  
 
  
