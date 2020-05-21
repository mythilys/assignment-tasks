print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------------STUDENT REPORT CARD---------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
var=int(input("enter the roll number:"))
var1=input("enter the name:")
m1=int(input("enter the tamil mark:"))
m2 = int(input("enter the english mark:"))
m3 = int(input("enter the maths mark:"))
m4 = int(input("enter the science mark:"))
m5 = int(input("enter the social mark:"))
total=m1+m2+m3+m4+m5
average=total/5
print("ROLL NUMBER:",var)
print("NAME:",var1)
print("TAMIL MARK:",m1)
print("ENGLISH MARK:", m2)
print("MATHS MARK:", m3)
print("SCIENCE MARK:", m4)
print("SOCIAL MARK:", m5)
print("TOTAL:", total)
print("AVERAGE:", average)
if average >=80:
    print("GRADE-A")
elif average >=70:
    print("GRADE-B")
elif average >=60:
    print("GRADE-C")
elif average >=50:
    print("GRADE-D")
elif average >=40:
    print("GRADE-E")
elif average <=30:
    print("GRADE-F")
