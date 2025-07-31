f = open("poem.txt", "r")
content = f.read()

if("twinkle" in content):
    print("twinkle is present")
else:
    print("Twinkle is not present")
f.close()