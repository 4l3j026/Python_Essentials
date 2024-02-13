# Fast food Resturant exercise using dictionary 
print("Hello everyone and welcome to Prehistoric Fast Food!")
#Show the user menu
print("""
      
    1.  Triceratops Burguer =  $10.80 
    2.  Brontosaurus Hot Dog = $18.60
    3.  Velociraptor Sandwich = $8.00
    4.  Tyrannosaurus Fries = $20.50
    5.  Stegosaurus Pizza = $30.40
      
      """)

Option = input("Would you like to order? (Y/N): ")
 
while Option == 'Y' or Option == 'y':
        
    user_option = int(input("Select your option, entering a integer number of menu: ")) #Take input data


