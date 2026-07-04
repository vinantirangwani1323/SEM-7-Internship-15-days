print(" Hello,World ")

a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))
c = a + b
d = a - b
e = a * b
f = a / b
print("A value is:", a, "\nB value is:", b, "\nSum is:",c ,"\nSum is:",c ,"\nDiff is:",d , "\nMul is:",e , "\nDiv is:",f)

x = str("Hii")
y = int(5)
z = float(2.5)
print(type(x))
print(type(y))
print(type(z))

a = "Hello World"
print(a[2:5])
print(a[:2])
print(a[5:])
print(a[-1:])
print(a.replace("H","J"))
print(a.lower())
print(a.strip())
print(a.split(","))


g = 50
g = g + 10
print(g)

h = 10
j = 5
if j > h:
 print("j is greater")
else:
 print("h is greater")

i = 3
k = 4
print(i & k)
i = 6
print(i > 5 and i < 10)

list = ['apple', 'mango', 'banana']
print('apple' not in list)
print('kiwi'  in list)