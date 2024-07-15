print("Marksheet..")
name=(input("enter your name:"))
seatno=int(input("enter your seat number:"))
print("All subject marks out of 100")
a=int(input("python mark:"))
b=int(input("java mark:"))
c=int(input("c++ mark:"))
d=int(input("php mark:"))
e=int(input("seo mark:"))
if(a>=30 and b>=30 and c>=30 and d>=30 and e>=30):
    total=a+b+c+d+e
    print("total marks out of 500 are:",total)
    per=total*100/500
    print("percentage:",per)
    if(per>=80):
        print("pass with A grade")
    elif(per<=79 and per>=60):
        print("pass with B grade")
    elif(per<=59 and per>=30):
        print("pass with C grade")
    else:
        print("pass with D grade")
else:
    print("sorry you are fail..")
