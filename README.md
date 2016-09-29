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
The script is broken down into a section of main code and a series of functions that execute the repeated actions.  In the main code, there are two while loops: 1)run while the user elects to continue playing and 2)run while the user has not guessed the word. In the inner loop, the user is first prompted to choose the method by which the word to be guessed is set.  `random` selects a word from a small hard-coded list, while `player2` allows a second user to enter a word to be used while masking the input on screen.  Empty lists for the formatted guessed letter output, the unformatted guessed word, and the max number of guesses are initialized.  In the inner loop,  the user is prompted with the current ASCII, the current progress on the word, the number of guesses remaining and then asked to make a guess.  The current progress on the word is printed with a group of 3 underscores for each letter in the word (underscore-letter-underscore for guessed letters).  Each guessed letter is evaluated against the word, the list of currently guessed letters is updated, and out is generated for the user confirming their guess as correct or incorrect.  If the playAgain() prompt in the outer returns yes, the loop continues, and if it returns no, then the code breaks out of the inner loop and exits.

The functions are as follows:
* setASCII() - modifies base ASCII for current guess number (adds body parts)
* printASCII() - prints ASCII array
* getLetter() - prompts the user for a guess (letter) and enforces only a-z input
* playAgain() - asks the user if they want to play again, enforces y/n input, and if no, breaks out of inner while loop
* selectMethod() - prompts user to choose method of play, enforces 'random' or 'player2' input
* verifyWord() - enforces a-z input for player2 method (no spaces or characters)

he base ASCII array will be modified with each unsuccessful guess.  I started with this sketch to define the skeleton array in the main code, while setASCII returns the original array modified based on the guess number to show the correct number of "body parts."  

![ASCII Sketch](/images/hangman_ascii.jpg)

##Screenshots

![Hangman1](/images/hangman1.png)
![Hangman2](/images/hangman2.png)
![Hangman3](/images/hangman3.png)
![Hangman4](/images/hangman4.png)
