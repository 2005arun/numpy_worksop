#write a program to find if the given number is prime no or not
n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    else:
        continue
if flag==1:
    print("no")
else:
    print("prime")
