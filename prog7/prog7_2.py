#Use mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File name does not exist!")
    quit()

sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    start = line.find('0')
    num = float(line[start:])
    sum = sum + num
    count = count + 1

average = sum / count
print("Average spam confidence:",average)
