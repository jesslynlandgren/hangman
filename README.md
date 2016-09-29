#Hangman Command Line Game

##Summary:
This project is a version of the traditional [hangman game](https://en.wikipedia.org/wiki/Hangman_(game)) that is played via the command line, which is often an exercise given to new coders.

The user runs the python script to begin the game, and is guided via prompts to either enter or generate a word to guess, make guesses one letter at a time, and choose whether to play again at the end of the game.

##Requirements:
The project was completed as part of the Python curriculum for Digital Crafts, so the majority of the requirements were set in the exercise instructions.
* Have an ASCII representation of a "hangman".
* Follow the ASCII representation with a visual representation of the word being guessed.
* Update both the ASCII and word representation after every guess.
* Allow another person to enter a word while masking the input.
* Allow repeated play with a fresh word without restarting the script.
* Limit the number of guesses per word (correct guesses do not count against this total).

##Walkthrough

###What was used:
* Python:
  - random
  - getpass
  - warnings
