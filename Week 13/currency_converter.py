"""
    Name: currency_converter.py
    Author: Noel Onate
    Created: 11/13/25
    Purpose: Hub for converting currencies into other ones
"""

# Create constants for program
CURRENCIES = ["Dollars", "Yen", "Euros"]
DOLLARS_TO_YEN = 154.50
DOLLARS_TO_EUROS = 0.86
YEN_TO_EUROS = 0.0056

# ------------------------- MAIN FUNCTION ----------------------------- #
def main():
    # Print title screen
    print("******************************")
    print("*     CURRENCY CONVERTER     *")
    print("******************************")

    # Start loop
    while True:
        # Ask user what they are converting from
        print("\nConvert from:")
        display_options()
        convert_from = int(input(">> "))

        # Ask user to input amount
        amount = float(input("\nEnter amount: "))

        # Ask user what they are converting to
        print("\nConvert to:")
        display_options()
        convert_to = int(input(">> "))

        # Pass user inputs as arguments for function
        conversion_amount = convert(convert_from, convert_to, amount)

        try:
            # Try to display results
            print(f"\n{amount} {CURRENCIES[convert_from - 1]} is {conversion_amount:,.2f} {CURRENCIES[convert_to - 1]}.")
            
        except:
            # Should an error occur, the user likely typed an invalid currency. So, restart loop
            print("\nYou entered an invalid currency!")
            continue
        
        # Ask user if they would like to do another conversion
        choice = input("\nWould you like to do another conversion? (Y/N): ")

        # If they say yes, continue loop. Otherwise, exit loop/program
        if choice.upper() == "Y":
            continue
        else:
            break

# ------------------------- DISPLAY OPTIONS ----------------------------- #
def display_options():
    for currency in range(len(CURRENCIES)):
        print(f"{currency + 1}. {CURRENCIES[currency]}")

# ------------------------- CONVERT ----------------------------- #
def convert(convert_from, convert_to, amount):
    # Convert from Dollars
    if convert_from == 1:
        # To Dollars
        if convert_to == 1:
            return amount
        
        # To Yen
        elif convert_to == 2:
            return amount * DOLLARS_TO_YEN
        
        # To Euros
        elif convert_to == 3:
            return amount * DOLLARS_TO_EUROS
        
    # Convert from Yen
    if convert_from == 1:
        # To Dollars
        if convert_to == 1:
            return amount / DOLLARS_TO_YEN
        
        # To Yen
        elif convert_to == 2:
            return amount
        
        # To Euros
        elif convert_to == 3:
            return amount * YEN_TO_EUROS
    
    # Convert from Euros
    if convert_from == 1:
        # To Dollars
        if convert_to == 1:
            return amount / DOLLARS_TO_EUROS
        
        # To Yen
        elif convert_to == 2:
            return amount / YEN_TO_EUROS
        
        # To Euros
        elif convert_to == 3:
            return amount


# Allow for use as a module
if __name__ == "__main__":
    main()