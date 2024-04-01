#Dictionary Task

def main (): #Main function
    
    Text_Input = input("Enter your text: ") #Input text 
    f = Input_Text(Text_Input)
    print(f)
    
    
    
    
def Input_Text (User_Text: str): #Create function 
    
    text_lower = User_Text.lower() #Convert text to lower case
    text_comas = text_lower.split() #Separate text by commas
    key_words = () #Create empty tuple
    key_words = text_comas #Assign the text to the tuple 
    
    word_counter = () #Create another empty tuple to save words counter
    
    # for word in key_words:
    #     word_counter[word] = key_words.count(word)
        
    #print(word_counter)
    
    # Final_Dictionary = {}
    
    # Final_Dictionary = User_Text

    return key_words


if __name__ == "__main__": #Important python line to execute the main function
    main()
    
    