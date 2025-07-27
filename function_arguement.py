def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)
    
    a = goodday("Harry", "Thank you")
    print(a)
    
    ##Default arguement
    
    def goodday(name, ending = "Thank you"):
        print(f"Good Day, {name}")
        print(ending)
        
        goodday("Gagan")