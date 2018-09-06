import re

fname = input("Enter file name:")

try:
    fh = open(fname)
except:
    print("File name does not exist!")
    quit()

s = 0
line = fh.read()
lst = re.findall('[0-9]+',line)

for i in lst:
    i = int(i)
    s = s + i

print(s)
