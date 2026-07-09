myfile = open("Vinanti.txt1", "w")
myfile.write("Hello Vinanti")
myfile.close()

file = open("Vinanti.txt1","a")
file.write("\nHello")
file.close()

f = open("Vinanti.txt1","r")
data = f.read()
print(data)
f.close()


fileNAME = input("Enter the file name:")
fileCont = input("Enter the content you want to print:")

efile = open(fileNAME, "a")
efile.write(fileCont)
efile.close()
