def f_to_c(f):
    return 5*(f-32)/9
    
f = int(input("Enter a temperature: "))
c = f_to_c(f)
print (f"{round(c, 2)} Degree C")
