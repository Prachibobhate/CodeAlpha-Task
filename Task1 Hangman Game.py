#TASK 1
# Hangman Game
import time  # Importing the time module to use sleep for pauses
import random  # Importing random to randomly select a word from the list

# Welcoming the user
name = input("What is your name? ")
print("Hello, " + name + ", Time to play hangman!")

# Wait for 1 second
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

# Set a list of secret words. You can choose any words you like.
words = ["happily", "softens", "innocent", "childish", "broken", "anger", "sad"]

# Randomly select a word from the list
word = random.choice(words)

# Create a variable with an empty value to store the user's guesses
guesses = ''

# Determine the number of turns
turns = 10

# Create a while loop to run the game
while turns > 0:         
    # Make a counter that starts with zero
    failed = 0             

    # For every character in the secret word    
    for char in word:      
        # See if the character is in the player's guess
        if char in guesses:    
            # Print the character
            print(char, end="")    
        else:
            # If not found, print a dash
            print("_", end="")     
            # Increase the failed counter with one
            failed += 1    

    # If failed is equal to zero, the player has won
    if failed == 0:        
        print("\nYou won!")  # Print You Won
        break  # Exit the game loop
    
    # Ask the user to guess a character
    guess = input("\nGuess a character:") 

    # Add the player's guess to the guesses string
    guesses += guess                    

    # If the guess is not found in the secret word
    if guess not in word:  
        # Decrease the turns counter by 1
        turns -= 1        
        # Inform the player they guessed wrong
        print("Wrong")  
        # Inform the player how many turns are left
        print("You have", turns, 'more guesses') 

        # If the turns are equal to zero, the player loses
        if turns == 0:           
            print("You Lose")
