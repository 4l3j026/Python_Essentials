# Dictionary Exercise


def main():

    dictionary_1 = {
        "Name": "Alejandro",
        "Age": 22,
        "Career": "Mechatronics Engineer",
        "Hobby": "Play Cello",
        "Favorite Color": "Green",
    }

    # Show current state of the dictionary
    print(dictionary_1)

    print(dictionary_1["Name"])  # Print only the name value

    dictionary_1["Hobby"] = "Dance"  # Change element inside the dictionary

    print(dictionary_1["Hobby"])  # Print the new value

    dictionary_1["Girlfriend"] = "Laura"  # Add new element

    # Show update dictionary
    print(dictionary_1)

    del dictionary_1["Favorite Color"]

    print(dictionary_1)

    Exist = "Favorite Color" in dictionary_1

    print(Exist)

    Exist = "Name" in dictionary_1

    print(Exist)


if __name__ == "__main__":

    main()
