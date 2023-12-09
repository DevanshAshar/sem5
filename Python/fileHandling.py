print("Enter 5 numbers")
List1 = list()
fileWrite = open("file1.txt", "w") # w means write (data override hoga) , r means read ,a means append (data override nhi hoga), r+ read and write a+ append and write 
for i in range(5):
 List1.append(int(input("Enter number : ")))
 fileWrite.write(str(List1[i]))
 fileWrite.write("\n")
fileWrite.close()
fileRead = open("file1.txt", "r")
List = list()
for line in fileRead:
 List.append(int(line))
List.sort()
print(List)
