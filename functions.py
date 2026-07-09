
def my_function(name, sname):
 print("My name is ", name ,"", sname)

my_function("Vinanti","Rangwani")


def my_country(countryName = "India"):
 print("My country name is", countryName)

my_country()


def my_calc(x,y):
 return(x + y)

result = my_calc(2, 13)
print(result)


def my_func():

 x = 100
 print(x)
my_func()



y = 100
def my_func():
 print(y)
my_func()
print(y)

x = 200
def myfunc():
 x = 400
 print(x)
myfunc()

print(x)
 
#print 1 to 10 without using loops
def callMe(nn):
 if nn>0:
  print(nn)
  nn = nn - 1
  callMe(nn)
callMe(10)
 
#sum and avg using the function
def pSum(a, b, c):
 d = a + b + c
 return d

def pAvg(total):
 avg = total/3
 return avg



no1 = int(input("Enter the No1:"))
no2 = int(input("Enter the No2:"))
no3 = int(input("Enter the No3:"))

ans = pSum(no1,no2, no3)
print("the sum is:",ans)

aavg = pAvg(ans)
print("The avg is:", aavg)
