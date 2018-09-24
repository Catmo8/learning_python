fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = dict()
email = list()
common_email = None

for line in fh:
    if not line.startswith('From '):
        continue
    email = line.split()
    count[email[1]] = count.get(email[1],0) + 1

maximum = max(count.values())

for i in count:
    if count[i] == maximum:
        common_email = i
print (common_email,maximum)
