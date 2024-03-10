""""
Tic Generation Dictionary Exercise Fast Food 
"""


def main():

    # Variables
    Total_Order = 0.0  # Initialize value of the order

    # Create dictionary
    fast_food_menu = {
        "hot dog": 5.00,
        "hamburger": 8.50,
        "big sausage and fries": 12.80,
        "french fries": 7.20,
        "soda": 2.80,
        "ice cream": 4.30,
    }

    print("\n\n     Welcome to this Fast Food Restaurant! \n\n")

    print("Food Menu:")

    for (
        Key_Word,
        Value,
    ) in fast_food_menu.items():  # Print each tuples of the dictionary

        print(f" -> {Key_Word}, Price: {Value}")

    while True:

        Product = input("\n  Enter an option: ")
        Product = Product.lower()
        Product = Product.strip()

        if Product in fast_food_menu:

            Total_Order += fast_food_menu[Product]
            print(f"Product value: ${fast_food_menu[Product]}")

        elif Product == "exit":

            print(f"Your total order is: ${Total_Order:.2f}")

            break

        else:

            print("The entered value is not valid!")


if __name__ == "__main__":

    main()
