# Function Example
def computepay(h,r):
    nPay = h
    xPay = 0
    if h > 40:
        nPay = 40
        xPay = h-40
    
    return nPay*r + xPay*r*1.5
 
hrs = float(raw_input("Enter Hours: "))
rHour = float(raw_input("Enter Rate x Hour: "))
print computepay(hrs,rHour)
