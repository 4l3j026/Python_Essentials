#Try Except exercise 

print("Welcome to this progrma user!")

try: 
    
  dividend = int(input("Enter the number to divide: "))

  divisor = int(input("Enter the divisor: "))
  
  result = dividend / divisor
  
except ZeroDivisionError as e: 
    
    print(e) 
    print("The division can't resolve if divisor is 0")
   
except ValueError as e: 
    
    print(e)
    print("Wrong value")

except Exception as e: #Only use this block is not a good practice 
    
    print(e)
    print("Something went wrong!") 
    
else:
    print(result)
    
finally: 
    
    print("\n\n Remember always keep learn!!! \n\n")
