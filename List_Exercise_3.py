#List exercise 
def main(): 
    
    store_list = []
    
    while True: 
        
        print("\n\n Welcome to this Electronic Store: \n")
        print(" 1. Add your product")
        print("\n 2. Delete your product")
        print("\n 3. View all products")
        print("\n 4. Exit of the menu")
        
        option = input("\n\nEnter your option: ")
        
        if option == "1":
            item = input("\nEnter your product: ")
            store_list.append(item)
            
        elif option == "2": 
            item = input("\nWhat product do you want to remove?: ")
            if item in store_list:
                store_list.remove(item)
                
        elif option == "3":
            print("\nYour list of products is: ")
            for item in store_list: 
                print(" - " + item)
                
        elif option == "4": 
            break
        
        else: 
            print("Your option is not valid.")
        
if __name__ == "__main__": 
    
    main()