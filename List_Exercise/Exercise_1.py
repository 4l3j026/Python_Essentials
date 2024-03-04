#Lists Exercise 

List_1 = [] #Create empty list (without elements)

for i in range(0, 3): 
   
    data = input(f"Enter random element {i + 1}: ") 
    
    List_1.append(data) #Method to add info to the list
    
print("The value of the list is: ", List_1)
