score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Please enter a number between 0.0 and 1.0")
    quit()

if (s < 0.0 or s > 1.0):
    print("Please enter a number between 0.0 and 1.0")
    quit()
elif s >= .9 :
    print("A")
elif s >= .8 :
    print("B")
elif s >= .7 :
    print("C")
elif s >= .6 :
    print("D")
else :
    print("F")
