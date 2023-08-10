import random

import string 

from Wordsforthehangmangame import wordsforthegame

from lives_visual import lives_visual_dictionary


def GetValidWord(wordsforthegame):

     #random word of the list
    word = random.choice(wordsforthegame)

    while '-' in word or ' ' in word:
        random.choice(wordsforthegame)

    return word.upper()    

    
def hangman():

    print("Cheerio and welcome to our humble abode, old chap!(Bri'ish accent)")
    print("Yes this is the hangman game blah blah blah wanna play? Yes? Ok.")

    word = GetValidWord(wordsforthegame)

    letters_to_guess = set(word)
    guessed_letters = set()
    alphabet = set(string.ascii_uppercase)

    lives = 7

    while len(letters_to_guess) > 0 and lives > 0:
      
        print(f"You have {lives} live(s) left. Letters already used: {' '.join(guessed_letters)}")

        word_list = [letter if letter in guessed_letters else '-' for letter in word]

        #Display the current state of the word
        print(lives_visual_dictionary[lives])
        print(f"Word: {' '.join(word_list)}" )

        users_letter = input("Choose a letter: ").upper()

        if users_letter in alphabet - guessed_letters:

            guessed_letters.add(users_letter)

            if users_letter in letters_to_guess:
                letters_to_guess.remove(users_letter)
                print(' ')
            else:
                lives -= 1
                print(f"\n Your letter ({users_letter}) is not in the word.")

        elif users_letter in guessed_letters:
            print("\nYou already chose that letter, choose a new letter.")
        
        else:
            print('\nThis letter is invalid.')

    # All letters already guessed or no lives left.
    if lives == 0:
        print(lives_visual_dictionary[lives])
        print(f"Hanged! The word was: {word}")  
    
    else:
        print(f"Splendid! You guessed the word {word}!")



hangman()















