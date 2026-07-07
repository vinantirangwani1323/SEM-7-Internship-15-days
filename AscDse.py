a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
c = int(input("Enter the number c:"))
d = int(input("Enter the number d:"))
e = int(input("Enter the number e:"))

nums = [a, b, c, d, e]
for i in range(len(nums)):
 for j in range(len(nums)-1):
  if nums[j] > nums[j+1]:
    nums[j], nums[j+1] =  nums[j+1], nums[j]

print("Asending:", nums)


nums = [a, b, c, d, e]
for i in range(len(nums)):
 for j in range(len(nums)-1):
  if nums[j] < nums[j+1]:
    nums[j], nums[j+1] =  nums[j+1], nums[j]

print("Desending:", nums)




