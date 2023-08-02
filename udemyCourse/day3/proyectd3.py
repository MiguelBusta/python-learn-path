"""
26/11/2022
Miguel Ángel Bustamante Pérez

Day 3 Project

Write a program that first asks the user to input a text. It can be any kind of text: an article, paragraph, phrase, poem, anything. Then, the program is going to ask the user that also enters three letters and then the code is going to process that information to create five analyisis and return the user the next info. 

1.- How many times does each letter that the user chose appears in text? (storage the letters in a list and then use some method of strings that allows to count how many times does a substring appears inside a string, remember to convert all the text to lowercase or uppercase). 

2.- How many words are in the text. To achieve this part remember that there is a string method that allows to transform it into a list and then, there is a function that allows to find the length of that list. 

3.- Return the first letter of the text and the last one. Use indexes.

4.- The system must show how the text will be if the order of words would be backwards. Is there any method that allows to reverse the order of a list, and another that allows to join those elements with spaces between them? 

5.- The system must identify if the word "Python" is found within the text. This part can be complex to imagine, but here is a clue: You can use Boolean values to make your research, a dictionary to find the way to express the user your answer. 
"""

def count_letters(text, characters):
    """
    Function that counts how many times does the chosen letters appear in text. 
    """
    # Format the text 
    text_low = text.lower()

    #Print how many times does the character appears in the text 
    for i in range(0, 3):
        print(f"The character: {characters[i]} is found: {text_low.count(characters[i])} times in text.")

def count_words(text):
    """
    Function that returns the number of words within the text.
    """
    #convert the text into a list 
    split_text = text.split()
    print(f"The number of words within the text is: {len(split_text)}")

def first_last_letter(text):
    """
    Function that returns the first and the last letter within the text. 
    """
    print(f"The first letter of the text is: {text[0]} and the last one is: {text[-1]}")

def backwards(text):
    """
    This function reverses the order of the given text. 
    """
    text_list = text.split()
    text_list.reverse()
    print(f"The reversed text is: {' '.join(text_list)}")

def find_python(text):
    """
    This function founds if the word 'Python' is found within the text. 
    """
    if text.find("Python") != -1:
        print("The Python word exists within the text.")
    else: 
        print("Python word was not found.")

def main():
    """
    Main function of the project.
    """
    # Enter the text and letters
    text = input("Please enter your text: ")
    characters = []
    for i in range(0, 3, 1):
        letter = input("Enter a letter: ")
        characters.append(letter.lower())
    # Analysis 1
    print("\nFunction 1")
    count_letters(text, characters)
    # Analysis 2
    print("\nFunction 2")
    count_words(text)
    #Analysis 3
    print("\nFunction 3")
    first_last_letter(text)
    #Analysis 4
    print("\nFunction 4")
    backwards(text)
    #Analysis 5
    print("\nFunction 5")
    find_python(text)

main()