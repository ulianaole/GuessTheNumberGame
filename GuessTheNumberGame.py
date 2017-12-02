# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
range_size = 100

# helper function to start and restart the game
def new_game():
    if range_size == 100:
        range100()
    else:
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_size
    global secret_number
    global number_of_guesses 
    range_size = 100
    secret_number = random.randrange(0, 100)
    number_of_guesses = 7
    print ""
    print "New game. Range is from 0 to 100."
    print "Number of remaining guess is 7." 
    print ""

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_size
    global secret_number
    global number_of_guesses
    range_size = 1000
    secret_number = random.randrange(0, 1000)
    number_of_guesses = 10
    print ""
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guess is 10." 
    print ""
    
def input_guess(guess):
    # main game logic goes here	
    global number_of_guesses
    guess = int(guess)
    number_of_guesses = number_of_guesses - 1
   
    print "Guess was " + str(guess)
    if guess < secret_number:
        print "Number of remaining guess is " + str(number_of_guesses)
        print "Higher"
    elif guess > secret_number:
        print "Number of remaining guess is " + str(number_of_guesses)
        print "Lower"
    else:
        print "Number of remaining guess is " + str(number_of_guesses)
        print "Correct"
        new_game()
            
    if number_of_guesses == 0:
        print "You ran out of guesses. The number was " + str(secret_number)
        new_game()     


    
# create frame
frame = simplegui.create_frame("Guess the number", 100, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.add_input("Your guess", input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
