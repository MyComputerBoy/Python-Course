"""Functions.py -> This is an introduction to functions in python
"""

#This is how to create a function called "Main"
def Main():
	print("This is the Main function")

#To call a function you write its name followed by parenthesis
Main()

#You can call a function any time however many times you want
Main()
Main()
Main()
#This will call the Main function 4 times in total in a row

#Functions can have arguments, or things to give it for it to work
#In this example the Add function expects two inputs
#InputA that should be a float and InputB that's also a float
#
#Note, the -> float part shows that it should return a float
def Add(InputA: float, InputB: float) -> float:
	Output: float = InputA + InputB

	#Functions can return values to make them more useful
	#To do that you can just write "return" then the value to return
	return Output

#Now to call the function
Add()
#This will create an error since the Add function expects two inputs, but none were given

#Now this won't since it was given the arguments it requires
Add(2.718281, 3.141592)

#Now this will also cause an error since it only expects two, no more, no less
#And since it's given three arguments, it doesn't know what to do with the last one
#So it causes an error
Add(2, 3, 5)
