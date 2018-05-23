#!/usr/bin/env python3
import sys
try:
    money = int(sys.argv[1])
    income = money - 3500
    if income > 0: 
        if income  > 80000: 
            tax = income * 0.45 - 13
        elif income  >= 55000 and money < 80000:
            tax = income * 0.35 - 5505
        elif income  >= 35000 and money < 55000:
            tax = income * 0.30 - 2755
        elif income  >= 9000 and money < 35000:
            tax = income * 0.25 - 1005
        elif income  >= 4500 and money < 9000:
            tax = income * 0.20 - 555
        elif income  >= 1500 and money < 4500:
            tax = income * 0.10 - 105
        else:
            tax = income * 0.03
        print(format(tax, ".2f"))
    else:
        print("0.00")
except:
    print("Parameter error")

