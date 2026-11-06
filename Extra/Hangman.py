import random
import time
#
#
#
#
#
#
#There are currently several (12) problems with this program. Some are "Logic problems" and some are random.
#These problems can range from code, to typos, to strings/input errors.
#Add all of your names to this program as a comment before one of your uploads.
def choose_word():
    with open("hangmangame/hangman bugfix/wordlist.txt", "r") as file:
        word_list = file.read().split(" ") #is it splitlines or split?...
    return random.choice(word_list)

def displayword(word, guessed_letters):
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += random.choice(letter)
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        display_word = displayword(word, guessed_letters)
        print(display_word)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Tries left: {tries}")
       

        if display_word == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess == word:
            print(f"Congratulations! You guessed the word: {word} correctly!")
            
        elif guess in word:
            guessed_letters.append(guess)
            
        else:
            guessed_letters.append(guess)
            tries -= 1
            if tries == 0:
                print("You're out of tries. The word was: " + word)
                break
    

print("Welcome to my Hangman Game!")
print("You have 6 tries to win the game!")
print("Good luck.")
time.sleep(3)
hangman()

#Mistake 1 deleted .choice()
#Mistake 2 changed spelling to import time
#Mistake 3 deleted the underscore and fixed location of file on line 13
#Mistake 4 changed it to a split function 
#Mistake 5 removed random string
#Mistake 6 included parameters
#Mistake 7 line 37 deleted
#Mistake 8 line 54 fixed tries
#Mistake 9 line 55 changed the > to ==
#Mistake 10 line 47 changed word sting to variable
#Mistake 11 line 47 changed incorrectly to correctly