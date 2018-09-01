fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
cnt_of_hrs = dict()
email = list()
time = list()

for line in fh:
    if not line.startswith('From '):
        continue
    email = line.split()
    time = email[5].split(':')
    cnt_of_hrs[time[0]] = cnt_of_hrs.get(time[0],0) + 1

tmp = list()
for key,value in cnt_of_hrs.items():
    tmp.append((key,value))

tmp = sorted(tmp)
for key,value in tmp:
    print(key,value)

    
