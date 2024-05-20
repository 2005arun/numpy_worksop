# find if the given number is a palindrome or not?
# n=int(input())
# a=str(n)
# if n==int(a[::-1]):
#     print("palindrome")
# else:
#     print("Not")
n=input()
if n==n[::-1]:
    print("palindrome")
else:
    print("no")