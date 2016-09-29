#Hangman Command Line Game

##Summary:
This project is a version of the traditional [hangman game](https://en.wikipedia.org/wiki/Hangman_(game)) that is played via the command line, which is often an exercise given to new coders.

The user runs the python script to begin the game, and is guided via prompts to either enter or generate a word to guess, make guesses one letter at a time, and choose whether to play again at the end of the game.

##Github Link
[Hangman Game](https://github.com/jesslynlandgren/hangman)

###What was used:
* Python:
  - random
  - getpass
  - warnings

##Requirements:
* Python 2 or Python 3

##Goals:
The project was completed as part of the Python curriculum for Digital Crafts, so the majority of the requirements were set in the exercise instructions.
* Have an ASCII representation of a "hangman".
* Follow the ASCII representation with a visual representation of the word being guessed.
* Update both the ASCII and word representation after every guess.
* Allow another person to enter a word while masking the input.
* Allow repeated play with a fresh word without restarting the script.
* Limit the number of guesses per word (correct guesses do not count against this total).

##Walkthrough
The script is broken down into a section of main code and a series of functions that execute the repeated actions.  In the main code, we first set the base ASCII array that will be modified with each unsuccessful guess.  I started with this sketch to define the skeleton array in the main code, while setASCII returns the original array modified based on the guess number to show the correct number of "body parts."  

[hangman_ascii.jpg]

When the user runs the script, they are prompted to choose the method by which the word to be guessed is set.  `random` selects a word from a small hard-coded list, while `player2` allows a second user to enter a word to be used while masking the input on screen.  The max number of guesses is 6 (due to the ASCII selected).  The user is prompted with the current ASCII, the current progress on the word, the number of guesses remaining and then asked to make a guess.  The

The functions are as follows:
* setASCII():
* printASCII()
* getLetter()
* playAgain()
* selectMethod()
* verifyWord()

##Screenshots
