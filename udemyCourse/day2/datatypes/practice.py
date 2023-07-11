myNumber1 = 1
print(myNumber1)
#function that returns the type of the given data
print(type(myNumber1))

myNumber2 = 5.8
print(myNumber2)
print(type(myNumber2))

#Change the value of the float number
myNumber2 = myNumber2 + myNumber1
print(myNumber2)
print(type(myNumber2))

age = input("Enter your age: ")
print("Your age is: " + age)

#Input returns a string value so in order to operate it as an integer you have to change that data into int
newAge = int(age) + 1
print(f"The next year you will be:",newAge)

#Implicit conversion
num1 = 20
num2 = 30.5
num3 = num1 + num2
print(type(num1))
print(type(num2))
print(type(num3))

#floors the value to its lower int value
print(int(num2))