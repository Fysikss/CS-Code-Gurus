"""
    Name: coinflip.py
    Author: Noel Onate
    Created: 10/30/25
    Purpose: Simulate a game or games of a coin flip
"""

# Import randint function
from random import randint

# Global variable for starting user balance
STARTING_BALANCE = 1000.00

# ---------------- MAIN FUNCTION ----------------- #
def main():
    # Call function to display title
    print_title()

    # Set user balance to the starting balance
    user_balance = STARTING_BALANCE

    # Start game loop
    while True:
        # Check if user balance is at 0
        if user_balance == 0.00:
            # If it is, end the game
            print(f"\nDarn! Looks like you lost it all! Goodbye!")
            break

        # Show user their current balance
        # Ask user if they would like to play a round
        print(f"\nYour current balance is ${user_balance:,.2f}")
        print("Would you like to play a round? (Y/N)")
        choice = input(">> ")

        # Make user input uppercase, and if it is a Y, continue the program
        if choice.upper() == "Y":
            print("\nSounds good! Good luck!")

        else:
            # If anything else is typed in, end the program
            print(f"\nSounds good! Your final balance was ${user_balance:,.2f}!")
            break
        
        # Run a function to play a round of the game and update the user balance
        user_balance = flip_coin(user_balance)
    

# ---------------- PRINT TITLE ------------------- #
def print_title():
    print("***+***+***+***++***+***+***+***")
    print("|    Welcome to the Casino!    |")
    print("***+***+***+***++***+***+***+***")

# ----------------- GAME ---------------------- #
def flip_coin(user_balance):
    # Start loop for user input validation
    while True:
        # Ask user to input what side they would like
        print("\nWhat side would you like? (H/T)")
        user_side = input(">> ")

        # If user does not type a valid side, restart loop
        if user_side.upper() not in ["H", "T"]:
            print("Please enter either H or T!")
            continue

        # Otherwise, exit loop
        else:
            break
        
    # Start a second loop for user input validation
    while True:
        # Ask user to place a wager
        print("\nNow, how much would you like to wager?")
        print(f"Current Balance: ${user_balance:,.2f}")
        user_wager = float(input(">> "))

        # If the user types a wager larger than their balance or a negative, restart loop
        if user_wager > user_balance or user_wager < 0:
            print("\nPlease enter a positive wager less than or equal to your current balance!")
            continue

        # Otherwise, exit loop
        else:
            break
    
    # "Flip" a coin using randint
    outcome = randint(1, 2)

    # User wins their wage if it is a 1
    if outcome == 1:
        print(f"\nCongratulations! You won ${user_wager:,.2f}!")
    
    # Make the user wager to negative if it is a 2
    else:
        print(f"\nDarn! You lost ${user_wager:,.2f}!")
        user_wager *= -1
    
    # Add the user_wager value to the user balance, return the result
    return user_balance + user_wager

# ------------- START PROGRAM -------------- #
main()