#This is a comment starting with a #

#To print to the terminal
print("Hello World!")

#This is a string
StringVariableName: str = "Hello World!"

#This is how to print a variable to the terminal
print(StringVariableName)

#This is a number
IntVariableNameA: int = 127          #Int is a whole number only
FloatVariableNameB: float = 255.99   #Floats are numbers with a decimal too

#This is how to add two numbers and print it to the terminal
print(IntVariableNameA + FloatVariableNameB)

#This is how to get an input from the user and writing the prompt
StringUserInput: str = input("Write a name: ")

#How to write a more complex string to the terminal
print("This is your name %s." % (StringUserInput))

#This is a boolean, basically only true or false
BoolVariableNameA: bool = False
BoolVariableNameB: bool = True

#This is a list
ListVariableName: list = [2,3,5,7,11]

#How to get an item from a list
print(ListVariableName[0])
print(ListVariableName[1])
print(ListVariableName[2])

#This is how to convert a string from the user to an int
IntVariableNameC = int(input("Write a whole number: "))

#This is a function that you can call at any time
#Note the tab is very important in python
def Main():
  print("This is a function")
  return 1

def GetUserInput(UserPrompt: str = "") -> int:
  InputInt: int = int(input(UserPrompt))
  return InputInt

#And now to call the Main() function
Main()
Main()
Main()


print(GetUserInput("Write a number: ") + GetUserInput("Write another number for me please: "))
