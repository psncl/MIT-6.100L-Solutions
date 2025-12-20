# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return all(ch in set(letters_guessed) for ch in secret_word)


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    fuzz_guess = ""
    for ch in secret_word:
      fuzz_guess += ch if ch in letters_guessed else "*"
    
    return fuzz_guess


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return ''.join([ch for ch in string.ascii_lowercase if ch not in letters_guessed])

def correct_guess(secret_word, guess):
  """
  secret_word: string, the lowercase word the user is guessing
  guess: single letter that the user has guessed in one round

  returns: True if the secret word contains the guessed letter. False if it doesn't, or if the guess is longer than one letter.
  """
  if len(guess) > 1:
    return False

  return guess in secret_word

def reveal_letter(secret_word, available_letters):
  choose_from = "".join(set(secret_word).intersection(set(available_letters)))
  new = random.randint(0, len(choose_from) - 1)
  return choose_from[new]

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 10
    letters_guessed = []
    
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while guesses_left > 0 and not has_player_won(secret_word, letters_guessed):
      print("--------------")
      print(f"You have {guesses_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")

      guessed_letter = input("Please guess a letter: ")

      if len(guessed_letter) > 1 or (not guessed_letter.isalpha() and (with_help and guessed_letter != '!')):
        print("Oops! That is not a valid letter. Please input a letter from the alphabet:")
        
      elif guessed_letter == '!' and with_help:
        if guesses_left < 3:
          print("Oops! Not enough guesses left:")
        else:
          revealed_letter = reveal_letter(secret_word, get_available_letters(letters_guessed))
          print(f"Letter revealed: {revealed_letter}")
          letters_guessed.append(revealed_letter)
          guesses_left -= 3
          
      else:
        guessed_letter = guessed_letter.lower()

        if guessed_letter in letters_guessed:
          print("Oops! You've already guessed that letter:")
        else:
          letters_guessed.append(guessed_letter)

          if correct_guess(secret_word, guessed_letter):
            print("Good guess:")
          else:
            print("Oops! That letter is not in my word:")
            vowels = {'a', 'e', 'i', 'o', 'u'}
            guesses_left -= 2 if guessed_letter in vowels else 1

      
      print(f" {get_word_progress(secret_word, letters_guessed)}")

    print("--------------")
    if has_player_won(secret_word, letters_guessed):
      total_score = (guesses_left + 4 * len(set(secret_word))) + (3 * len(secret_word))

      print("Congratulations, you won!")
      print(f"Your total score for this game is: {total_score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

