x=2
marks=67
grades=89
marks=100
#if statement
if x>0:
    print("The number is positive")
#if..else statement
if marks>=60:
    print("you have passed")
else:
    print("you have failed")
#If...elif..else
if grades<=29 and grades>=0:
    print("you have failed")
elif grades<=49 and grades>=30:
    print("you have passed")
elif grades<=79 and grades>=50:
    print("you have credid")
elif grades<=100 and grades>=80:
    print("you have distincion")
else:
    print("wrong input")
if marks<=450 and marks>=400:
    print("qualified to national school")
elif marks<=400 and marks>=350:
    print("qualified to extra county school")
elif marks<=350 and marks>=300:
    print("qualified to county school")
elif marks<=300 and marks>=250:
    print("qualified to sub-county school")
elif marks<=250 and marks >=200:
    print("qualified to local school")
elif marks<=200 and marks >=100:
    print("you need to go back to school and start again")
else:
    print("not qualified at all")

