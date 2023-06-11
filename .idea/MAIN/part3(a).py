# Method 1 ✅
# need to test time complexity

File1 = open("file1.txt","r")
File2 = open("file2.txt","r")

Dic1 = File1.read().split()
Dic2 = File2.read().split()

print(Dic1)
print(Dic2)

DF = [ x for x in Dic1 if x not in Dic2 ]
DF2 = [ x for x in Dic2 if x not in Dic1 ]

print("Different words:")
print(DF)
print(DF2)

#Method 2

