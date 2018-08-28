fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File name does not exist!")
    quit()
    
lst = list()

for line in fh:
    line = line.rstrip()
    temp  = line.split()
    for i in temp:
        lst.append(i)

lst.sort()
print(lst)
