import math

while True:
    print("what operation would you like to proceed with? enter \"KILL\" to exit calculator")
    k=input()
    if k=="KILL":
        break
    if k in ("+","-","/","*","**"):
        print("enter value 1 to perform __",k,"__")
        v1=int(input())
        print("enter value 2 to perform ",v1,k,"__")
        v2=int(input())
        if k=="+":
            print(v1+v2)
        elif k=="-":
            print(v1-v2)
        elif k=="*":
            print(v1*v2)
        elif k=="/":
            print(v1/v2)
        elif k=="**":
            print(math.pow(v1,v2))
    if k =="sqrt":
        print("enter value for which you want to find square root")
        v1=int(input())
        print(math.sqrt(v1)) 