#This is a comment starting with a #

#To print to the terminal
print("Hello World!")

#This is a string
###################################################################################
#Note, the ": str" part is only to signal the user what type the variable should be
#But, the variable can still be other types without raising any errors, it is only a hint in python
StringVariableName: str = "Hello World!"

#This won't cause an error
StringVariableName = 233.45

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
#Note, list indexing starts at 0, meaning the first element is called by 0, not 1
print(ListVariableName[0])
print(ListVariableName[1])
print(ListVariableName[2])

#If you want to add more items to a list you can call append() to the list
ListVariableName.append(13)
ListVariableName.append(17)

#And to remove an item from a list you can call pop()
ListVariableName.pop(3) #Note, this will pop the fourth element since list indexing starts at 0

#This is how to convert a string from the user to an int
IntVariableNameC = int(input("Write a whole number: "))
FloatVariableNameC = float(input("Write a floating point number: "))

#This is a function that you can call at any time
#Note the tab is very important in python
#The tab signals everything like loops, if statements and such where and when they start and stop
def Main():
  print("This is a function")
  return 1

#You can call the functions whatever you want, and create as many as you want
def GetUserInput(UserPrompt: str = "") -> int:
  InputInt: int = int(input(UserPrompt))
  return InputInt

#And now to call the Main() function
Main()
Main()
Main()


print(GetUserInput("Write a number: ") + GetUserInput("Write another number for me please: "))

#This is a class
class Test:
  #This is to initialise the class with information that it need
  def __init__(self, Name: str, Age: float):
    self.Name = Name
    self.Age = Age

  #This is to make it into a string for users to read
  def __str__(self):
    return "Name: " + str(self.Name) + ", age: " + str(self.Age)

TestHandler = Test()
print(str(TestHandler))

#And to import libraries from other python programs within the runtime folder
#We can use import (python file name) to import all the different functions and classes
import LibraryForImports

#And to use the functions and classes in a library just use the library name . the function name
#This library has the class "Maths" which contains different mathematical functions such as the SquareRoot function
LibrarySquareRoot: float = LibraryForImports.Maths.SquareRoot(10)

#This computes the natural logarithm of the input (LibrarySquareRoot)
LibraryLogarithm: float = LibraryForImports.Maths.NaturalLogarithm(LibrarySquareRoot)

#Which we can the print to the terminal
print(LibraryLogarithm)

#For loops can be very useful for iterating through lists, or going through a range
#For example if you wanna show all the items in the ListVariableName list you can
#Use the for loop, creating a variable that you use in place for the items you get from the list, and giving the name of the list like this
for Item in ListVariableName:
  print(Item)

#You can also just go through a range of numbers using the range() function
for i in range(100):
  print(i)
#Note, the range() function starts by default at 0 and goes through every number except the one given
#So this will go from 0 to 99

#You can also look through the different files in the repository for a deeper look at the different things you can do in python
