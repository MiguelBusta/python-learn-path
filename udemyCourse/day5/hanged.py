"""
Date: 17/10/2023
Miguel Ángel Bustamante Pérez

* Hangman game

TODO: The program is going to choose a secret word and is going to show to the player an amount of hyphens (-) that represent the amount of letters that the word contains. Each turn, the player must chose a letter, if the letter is found inside the hidden word, the system is going to show the position of the letter in the word. But if the player inputs a letter that is not inside the text, it loses 1 hp. If the hp is equal to 0, then the game is over.

Comments:
Import the choice method, this is going to be needed in order to make the system chose randomly a word within a list of words.

Create as many functions as you consider necessary for the program to work properly.
"""

import random

def generate_hidden_words(word):
    """
    todo: this function will return the word hidden with hyphens.
    """
    hidden_word = ""
    for letter in word:
        hidden_word += "-"
    return hidden_word

def is_letter_valid(letter, word):
    """
    todo: Check if the letter is inside the word
    """
    return letter in word

def draw_letter(letter, word, hidden_word):
    """
    todo: Draw the new word with the found letters
    """
    word_as_list = list(word)
    hidden_word_as_list = list(hidden_word)

    for i in range(0, len(word_as_list)):
        if letter == word_as_list[i]:
            hidden_word_as_list[i] = letter
        else:
            continue

    # Transform the list into a string
    hidden_word = "".join(hidden_word_as_list)
    return hidden_word

def main():
    """
    Main function
    """
    # * Variables to use:
    hp = 6
    words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]
    word = random.choice(words_list)

    print("Welcome to the Hangman game\n")
    hidden_word = generate_hidden_words(word)
    print("The guess word is the following: ")
    print(hidden_word)
    while hp > 0:
        letter = input("Please enter a letter: ")
        if is_letter_valid(letter, word):
            hidden_word = draw_letter(letter, word, hidden_word)
            print(f"The word is now equal to: {hidden_word}")
            if hidden_word == word:
                print(f"Success you've won!!!")
                break
        else:
            hp -= 1
            print(f"Error your hp is now: {hp}")
    print("Thanks for playing <3")

if __name__ == "__main__":
    main()