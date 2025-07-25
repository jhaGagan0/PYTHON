print("Enter your marks")

a = int(input("Marks of maths: "))
b = int(input("Marks of science: "))
c = int(input("Marks of English: "))

# Calculate average correctly and use proper logical operators
if ((a + b + c) / 3 >= 40) and (a >= 33) and (b >= 33) and (c >= 33):
    print("Pass")
else:
    print("Fail")
