# Write a program that asks two questions that requiere a single word as an answer for each one, then returns the resultant name of the beer
# by combining those two answers in order to form create it. 

#The output message should look like this: 

# >> The beer's name is: 
# >> "answer1 answer2"


def main(): 
    """Beer's name program"""
    print("The beer's name is: " + "\n\"" + input("Write a pets name: ") + " " + input("Write the name of your favorite food: ") + "\"")

main()