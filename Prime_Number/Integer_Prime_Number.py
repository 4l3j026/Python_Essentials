#Determining an integer number is positive and prime

print("\n Welcome to this program!")

number = int(input("Enter a number: "))

if number <= 1: #Number 0 and 1 is not prime number
    
    print("The number entered is not prime.")
    
elif number == 2:
    print("The number entered is a prime:") #The number 2 is the n
    
else: 
    for i in range(2, number):
        if number % i == 0:
            print('The number entered is not prime.')
            break
        else:
            print("The number entered is prime.")
            break