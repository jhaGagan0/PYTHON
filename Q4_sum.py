n = int(input("Enter a number: "))

def sum(n):
    if(n==1 or n==0):
        return 1
    return sum(n-1)+n
print(f"The sum of this number is : {sum(n)}")