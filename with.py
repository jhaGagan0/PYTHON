f = open("file.txt")
print(f.read())
f.close()

# the same can be written using with

with open("file.txt") as f:
    print(f.read())
    
    #don't need to close the file