# no>1
#  number has only 2 factor "1" and itself

# 19=1 and 19=>prime number
# 24=> 1,2,4,7,not a prime number3

num=5
count=0 # ketla factor che by default zero declare
if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("Number is prime")
    else:
        print("Not a prime number")


