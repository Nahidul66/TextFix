##import datetime

x=datetime.datetime.now().day
y=datetime.datetime.now().month
z=datetime.datetime.now().year
b=int(input("Enter Day of Your Birth"))
c=int(input("Enter Month of Your Birth"))
d=int=int(input("Enter Year of Your Birth"))
if (z>d) and (x<b and y<c):
    print(b-x, "Days", c-y, "Month", z-d, "Years")
elif x<b and y>c:
    print(b-x, "Days", (c+12)-y, "Month", (z-1)-d, "Years")
elif x>b and y>c:
    print((b+30)-x,"Days", ((c+12)-1)-y, "Month", (z-1)-1,"Years")
elif x>b and y<c:
    print((b+30)-x, "Days", ((c-1)-1)-y, "Month", z-d, "Years")
else:
    print("Enter A Valid Data")
elif(d == z):
    if x < b and y > c:
        print(b-x, "Days", c-y, "Month", z-d, "Years")
elif (x<b and y>c):
    print(b-x, "Days", (c+12)-y, "Month")
elif (x>b and y>c):
    print((b+30)-x, "Days", ((c+12)-1)-y, "Month")
elif (x>b and y<c):
    print((b+30)-x, "Days", ((c-1)-1)-y, "Month")
else:
    print("Enter A Valid Data")

