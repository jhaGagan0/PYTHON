#Write a program to check whether a number is an Armstrong number or not.

a = int(input("Enter a number : "))
b = a
c = len(str(a))
sum = 0

while b > 0:
    digit = b % 10
    sum += digit ** c
    b = b // 10

if sum == a:
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
