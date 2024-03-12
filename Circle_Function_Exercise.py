#Calculate the circle area 

import math #Import math functions use this line

def main (): #main function 
    
    print("""Welcome user to this exercise! \n\n
          
            This program calculate the area of the circle entering radius of the circle: \n\n
          
          """) #User message 
    
    data_user = float(input("Radius value (in m): "))
    
    area_C = circle_area(data_user) #Call function 
    
    print(f"\nThe area of the circle is: {area_C:.2f} m2")
    
def circle_area (radius: float) -> float: #Funtion to calculate the area
    
    area = (math.pi * (radius ** 2)) #Equation 
    
    return area 
    

if __name__ == "__main__": #Important line to execute the main function
    
    main()