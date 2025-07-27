def greatest():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    
    if(a > b and a > c):
        print("Greatest number is " + str(a))
    elif(b > a and b > c):
        print("Greatest number is " + str(b))
    else:
        print("Greatest number is " + str(c))

# Call the function
greatest()
