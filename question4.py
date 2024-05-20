#write a program to find the sum of digits of a given number'
n=int(input())
a=str(n)
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
