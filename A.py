a=int(input("enter the number"))
if(a%2==1):
    print("weird")
elif((a%2==0)and(a>20)):
    print("not weird")
elif(a%2==0 and range(0,20)):
    print("NOT WEIRD")
elif(a%2==0 and range(21,40)):
    print("weird")
else:
    print("invalid input")
         
