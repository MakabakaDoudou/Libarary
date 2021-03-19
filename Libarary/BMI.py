# -*- coding: utf-8 -*-
h = float(input('please enter your height(m):'))
w = float(input('please enter your weight(kg):'))
BMI = w/h**2
print('your height is %.2fm, your weight is %.2fkg, your BMI is %d' %(h,w,BMI))
if BMI < 18.5:
    print('your BMI is over light')
elif 18.5 < BMI < 25:
    print('your BMI is normal')
elif 25 < BMI < 28:
    print('your BMI is over weight')
elif 28 < BMI < 32:
    print('your BMI is fat')
else:
    print('your BMI is over fat')
    print('please keep firt!')