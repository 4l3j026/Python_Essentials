#Try Except exercise 

print("Welcome to this progrma user!")

try: 
    
  dividend = int(input("Enter the number to divide: "))

  divisor = int(input("Enter the divisor: "))
  
  result = dividend / divisor
  
except ZeroDivisionError as a: 
    
    print(a) 
    print("The division can't resolve if divisor is 0")
   
except ValueError as a: 
    
    print(a)
    print("Wrong value")

except Exception as a: #This block is not a good practice 
    
    print(a)
    print("Something went wrong!") 
    
else:
    print(result)
    
finally: 
    
    print("Remember always keep learn!!!")
