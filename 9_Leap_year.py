num1=int(input("Enter the year:-"))

if (num1 % 400 == 0 ) and (num1 % 100 == 0 ):
    print("It is leap year",num1)
elif(num1 % 4 == 0):
    print("It is not leap year")
else:
    print("Not a valid number") 