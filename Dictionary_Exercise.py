""""
Tic Generation Dictionary Exercise Fast Food 
"""


def main():

    # Create dictionary
    fast_food_menu = {
        "Hot Dog": 5.00,
        "Hamburger": 8.50,
        "Big Sausage and Fries": 12.80,
        "French Fries": 7.20,
        "Soda": 2.80,
        "Ice Cream": 4.30,
    }

    print("\n\n     Welcome to this Fast Food Restaurant! \n\n")

    print("Food Menu:")

    for Key_Word, Value in fast_food_menu.items():
        print(f"-> {Key_Word}, Price: {Value}")


if __name__ == "__main__":

    main()
