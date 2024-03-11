# Exercise without vowels


def main():

    word_input = input("Enter a word: ")
    result = twttr(word_input)
    print("The word without vowels is: " + "".join(result))


def twttr(word: str) -> str:  # Create function to skip vowels

    word = word.lower()  # Lower words entered
    word = word.strip()  # Skip the spaces
    list_save = []  # Create empty list
    for i in range(len(word)):
        if word[i] not in ["a", "e", "i", "o", "u"]:  # Check if there are vowels
            list_save.append(word[i])

    return list_save  # Return value of the word


if __name__ == "__main__":  # It's important to use the main function in this file.
    main()
