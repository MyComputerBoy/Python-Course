"""Classes.py -> This is an introduction to how classes work in python

A class is just a convenient and useful way to store functions and variables in a singular place.
And having classes with one usage makes expectations and management of everything a lot easier.
That doesn't mean the classes themselves will be easy to implement, 
just that it doesn't need to worry about anything other than the one intended usecase
"""

#This is a class with a single variable
class StarterClass:
	TestString: str = "StarterClass string for testing"

#To access the variables and functions in a class just call the name of the class followed by a "." and the name of the variable/function
#In this case the class is called StarterClass and the variable we want is called TestString, so we call StarterClass.TestString
print(StarterClass.TestString)

#Classes have special functions in them that can make the classes much easier to work with in python
#These are called "dunder" methods, a short for Double Underscore methods
#For example, to initialise a class with a set of variables
#Create a method called __init__()
#Which is pronounced "dunder init" for Double Underscore init, or __init__
class TestClass:
	def __init__(self, Name: str, Age: float) -> None:
		#Now to have variables that are accessible from the whole class
		#We need to work with the "self" object, in other words we can save variables to the "self" object
		#And we can get variables from it
		
		self.Name: str = Name
		self.Age: float = Age

		#Here we set the Name and Age in the TestClass from the arguments we gave the dunder init function
	
	#Imagine if we wanna be able to change the name if the class
	#We can make a new function that changes the name by giving it a new name from the user
	def ChangeName(self) -> None:
		self.Name = input("What should the new name be? ")
	
	#We can do the same thing with the age
	def ChangeAge(self) -> None:
		self.Age = float(input("What should the new age be? "))
	
	#We can also make conversion to strings easy with a dunder str (__str__)
	def __str__(self) -> str:
		#Here we make the string where it says Name: then the name, Age: then the age
		return ("Name: %s, Age: %s" % (self.Name, self.Age))

#Classes can even use other classes for making even more complex and useful interactions
class RoomOfPeople():
	def __init__(self, People: list[TestClass] | None) -> None:
		#The proper way to check if a list is properly declared or not
		if People is None:
			self.People: list = []
		else:
			self.People: list[TestClass] = People
		
		#Here we have initialised the class with some people in a list
		#With this we can make many more interesting things than we otherwise could
	
	def AddAPerson(self, Person: TestClass) -> None:
		#Here we append the person to the list of people we have in the clas
		self.People.append(Person)
	
	#This function makes removing a person from the list possible
	def RemovePerson(self, Index: int) -> None:
		self.People.pop(Index)
	
	#Imagine if we wanna make a list of all people that the class have
	#Then we can create this function where it loops over every person in the list
	#And prints the string representation of the person
	def ShowAllPeople(self) -> None:
		for Person in self.People:
			print(str(Person))

