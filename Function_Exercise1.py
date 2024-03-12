#Exercise 1

def main ():
    
    re = Name_Hello("Alejo")
    print(re)   
    
    
def Name_Hello (Name: str) -> str: 
    
    regards = "Hello " + Name + ", and welcome to this important event!"
    
    return regards 
    
    
if __name__ == "__main__":
    
    main()