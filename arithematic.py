#Write a program to enter two integers, two floating numbers and then perform all arithmetic operations on them.

# Input
a = int(input("Enter 1st integer: "))
b = int(input("Enter 2nd integer: "))
c = float(input("Enter 1st floating number: "))
d = float(input("Enter 2nd floating number: "))

print("\n=== ARITHMETIC OPERATIONS ===")

# Addition
print(f"Addition: {a} + {b} = {a + b}")
print(f"Addition: {c} + {d} = {c + d}")
print(f"Addition of all: {a} + {b} + {c} + {d} = {a + b + c + d}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Subtraction: {c} - {d} = {c - d}")

# Multiplication
print(f"Multiplication: {a} × {b} = {a * b}")
print(f"Multiplication: {c} × {d} = {c * d}")
print(f"Multiplication of all: {a * b * c * d}")

# Division
print(f"Division: {a} ÷ {b} = {a / b}")
print(f"Division: {c} ÷ {d} = {c / d}")

# Floor Division
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulus
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Exponentiation: {c} ** 2 = {c ** 2}")
