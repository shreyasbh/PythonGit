# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for word in set(secretWord):
        if word not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for i in secretWord:
        if i in lettersGuessed:
            guessedWord = guessedWord + i + " "
        else:
            guessedWord = guessedWord + "_" + " "
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    total = list("abcdefghijklmnopqrstuvwxyz")
    for i in lettersGuessed:
        if i in total:
            total.remove(i)
    return ''.join(total)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    game = True
    guesses = 8
    lettersGuessed = []
    print("Welcome to the game, Hangman.")
    print("I am thinking of a word that is %d letters long." %(len(secretWord)))
    goodGuess = False
    while guesses > 0 and game :
        goodGuess = False
        print("-----------")
        print("You have %d guesses left" %(guesses))
        print("Available letters: %s" %(getAvailableLetters(lettersGuessed)))
        guess = input("Please guess a letter: ")
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue
        if guess in secretWord:
            print("Good guess :" + getGuessedWord(secretWord, lettersGuessed))
            goodGuess = True
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        if (isWordGuessed(secretWord, lettersGuessed)):
            game = False
        if not goodGuess:
            guesses -= 1
    
    print("-----------")
    if game == False:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was %s." %(secretWord))





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = "antler"
#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
