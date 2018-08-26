def computepay(h,r):
    if h <= 40:
        p = h * r
        return p
    else:
        reg_pay = 40 * r
        ot_hrs  = h - 40
        ot_rate = r * 1.5
        ot_pay  = ot_hrs * ot_rate
        p = reg_pay + ot_pay
        return p

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter numeric output!")
    quit()

p = computepay(h,r)
print(p)
