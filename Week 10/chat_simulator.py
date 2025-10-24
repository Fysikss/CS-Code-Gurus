"""
    Name: chat_simulator.py
    Author: Noel Onate
    Created: 10/23/25
    Purpose: Simulate a chat log with pickling
"""

# Import the pickle library
import pickle

# File name for chat log
FILE_NAME = "chat_log.pkl"

# Create empty list for chat log
chat_log = []

# Display title
print("+-----------------------------------------+")
print("|          AOL Instant Messenger          |")
print("+-----------------------------------------+")

# Ask user for username
username = input("Please enter your username: ")

# Unpickle the current chat log file
# Use try catch for exception if the file doesn't exist
try:
    with open(FILE_NAME, "rb") as file_handle:
        chat_log = pickle.load(file_handle)
    
    # Print the chat log
    for entry in range(len(chat_log)):
        print(chat_log[entry])
except:
    pass

# Start loop for chat log
while True:
    # Get message from user
    message = input("Enter message: ")

    # Append the username and message into list as one item
    chat_log.append(f"{username}: {message}")

    # Pickle the new list
    with open(FILE_NAME, "wb") as file_handle:
        # Write list to file with binary protocol
        pickle.dump(chat_log, file_handle)

    # Ask user if they would like to send another message
    choice = input("Send another message (Y/N)?")

    # If user says yes, restart loop
    if choice.lower() == "y":
        continue

    # Otherwise, exit loop
    else:
        break