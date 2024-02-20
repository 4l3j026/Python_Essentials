#Check palindrome 

s = input("Enter a number of string characters: ")

reverse_string = s[::-1]

if s == reverse_string:
    print("Is Palindrome")
else: 
    print("Is not Palindrome")
    