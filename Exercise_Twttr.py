# Exercise without vowels


def main():

    word_input = input("Enter a word: ")
    result = twttr(word_input)
    print("The word without vowels is: " + "".join(result))


def twttr(word: str) -> str:

    word = word.lower()
    word = word.strip()
    list_save = []
    for i in range(len(word)):
        if word[i] not in ["a", "e", "i", "o", "u"]:
            list_save.append(word[i])

    return list_save


if __name__ == "__main__":
    main()
