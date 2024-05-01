num=int(input("Enter the Number:-"))
rem=0
sum=0

while(num>0):
    rem=num%10
    sum=sum*10+rem
    num=num/10

    print("Reverse Number is:",sum)

