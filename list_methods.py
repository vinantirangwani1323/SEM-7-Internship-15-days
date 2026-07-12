list = ["A",1,"B",2, "C"]
list.append(3)
list.insert(6, "D")
list.remove("D")
list.pop(0)
d = list.count("D")
print(d)
print(list)

l2 = ["D",4,"E",3, "F"]
list.extend(l2)
print(list)

l = [5,8,10,4,7,6,1,8]
l.sort(reverse = True)
print(max(l))
print(sum(l))
print(min(l))
print(len(l))
print(l)

l5 = list.copy()
print(l5)