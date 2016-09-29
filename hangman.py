import random
import getpass
import warnings

def setASCII(guessNum):

    global frame
    if guessNum == 5:
        frame[1][1] = "O"
    if guessNum == 4:
        frame[2][1] = "|"
        frame[3][1] = "|"
    if guessNum == 3:
        frame[2][0] = "\\"
    if guessNum == 2:
        frame[2][2] = "/"
    if guessNum == 1:
        frame[4][0] = "/"
    if guessNum == 0:
        frame[4][2] = "\\"
    return frame

def printASCII(asciiArray):

    for row in asciiArray:
        print ''.join(row)

def getLetter():

    letter = raw_input("Guess a letter (a-z):  ")
    if letter.isalpha() and len(letter) == 1:
        return letter.lower()
    else:
        print "Only enter 1 lowercase letter a-z!"
        return getLetter()

def playAgain():

    again = raw_input("Do you want to play again? (y / n):  ")
    if again == 'y' or again == 'n':
        return again
    else:
        print "Only enter 'y' or 'n'!"
        return playAgain()

def selectMethod():
    print "CHOOSE PLAY METHOD"
    print "\tRandom: Computer selects word"
    print "\tPlayer2: Have a friend enter a word\n"
    method = raw_input("Enter choice ('random' or 'player2'):  ")

    if method == 'random' or method == 'player2':
        return method
    else:
        print "Only enter 'random' or 'player2'!"
        return selectMethod()

def verifyWord():
    word = getpass.getpass('Enter the word: ')
    word = word.lower()
    if word.isalpha():
        return word
    else:
        print "No tricks!  Single words with characters a-z ONLY!"
        return verifyWord()


frame = [[" ", "|", "-", "-", "|", " "],
         [" ", " ", " ", " ", "|", " "],
         [" ", " ", " ", " ", "|", " "],
         [" ", " ", " ", " ", "|", " "],
         [" ", " ", " ", " ", "|", " "],
         [" ", " ", " ", "-", "|", "-"]]

while True:

    print "\nPLAY HANGMAN!\n"
    method = selectMethod()
    warnings.filterwarnings("ignore")

    if method == 'random':
        words = ['yellow', 'space', 'science', 'notebook', 'digital', 'bottle', 'student', 'vehicle', 'window', 'pretzel']
        wordselect = random.randint(0, 9)
        word = words[wordselect]

    if method == 'player2':
        word = verifyWord()

    guessstr= ""
    numguess = 6
    progress = []
    guess = []

    i = 0
    for w in word:
        progress.append(" ___ ")
        guess.append('X')

    while guessstr != word and numguess>0:

        if numguess == 1:
            print 'You have {0} guess left\n'.format(numguess)
        else:
            print 'You have {0} guesses left\n'.format(numguess)

        printASCII(setASCII(numguess))

        j = 0
        printProgress = ""
        for let in progress:
            printProgress = printProgress + progress[j] + " "
            j += 1
        print printProgress
        print ""

        letter = getLetter()

        if letter not in word:
            print 'Nope, sorry!\n'
            numguess -= 1

        else:
            print "Good guess!\n"

            k = 0
            for w in word:
                if letter == w:
                    progress[k] = "_" + letter + "_"
                    guess[k] = letter;
                k += 1

            i = 0
            guessstr = ""
            for g in guess:
                guessstr += g
                i += 1

    if guessstr == word:
        print "YOU WIN"

    else:
        printASCII(setASCII(numguess))
        print "He's dead Jim! (You ran out of guesses) \n"

    choose = playAgain()
    if choose == 'y':
        frame = [[" ", "|", "-", "-", "|", " "],
                 [" ", " ", " ", " ", "|", " "],
                 [" ", " ", " ", " ", "|", " "],
                 [" ", " ", " ", " ", "|", " "],
                 [" ", " ", " ", " ", "|", " "],
                 [" ", " ", " ", "-", "|", "-"]]
        continue

    elif choose == 'n':
        break

print '\nBye!'
