#Index Method

#Variable to store the test string
myText = "This is a test"
result1 = myText[0]
result2 = myText.index("i")
result3 = myText.index("i", 4)


print(f"Printing a character: {result1}")
print(f"Printing the index of a character: {result2}")
print(f"Printing the index of a character using an start parameter: {result3}")