hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h <= 40:
    pay = h * r
else:
    reg_pay = 40 * r
    ot_hrs  = h - 40
    ot_rate = r * 1.5
    ot_pay  = ot_hrs * ot_rate
    pay     = reg_pay + ot_pay

print(pay)
