"""Loops.py -> This is an introduction to how loops work in python
"""

#This is just some setup for the different examples
NumberToGuess: int = 25
GuessedNumber: int = 0

#A while loop runs the loop as long as the condition is true
while NumberToGuess != GuessedNumber:
	#This while loop will run while the guessed number does not equal the number to guess
	GuessedNumber = int(input("Guess a number between 0 and 100: "))

#The for loop will loop through every item in the given list OR for the function given
#But, for now let's use the range() function for generating every number from 0 to in this case 10
for i in range(10):
	#The i we can call whatever we want, but it is customary to call it i when it's integers we're working with
	print(i)

#We can also change the interval and starting point of the loop by giving the range() function more variables
#The first number is the starting number
#The second is the maximum/minimum number
#The third is the interval the number should change by
for o in range(3, 100, 15):
	print(o)

#If we have a list of items we can loop through all of them with a for loop
Numbers: list[str] = ["One", "Three", "Nine", "Two Hundred"]
#Here we just need to give it the name of the list for it to work
for number in Numbers:
	print(number)


def CubicPolynomial(x: float) -> float:
	return 5*x**3 + 19.5*x**2 - 9*x + 3

def DerivativeOfCubicPolynomial(x: float) -> float:
	return 15*x**2 + 39*x - 9

TargetYValue: float = 25.24
EstimateX: float = 1

#While loops can easily be made to run infinitely if not handled properly
#Thus, it is always a good idea to have safety conditions and variables in place to ensure this does never happen
#It can be done by having a dedicated variable for managing if the loop should keep running and having extra conditions
#For the loop, like safety limits, for example this example should never have to be run more than a million times
#Or something has definitely gone wrong
while CubicPolynomial(EstimateX) != TargetYValue:
	EstimateX -= CubicPolynomial(EstimateX)/DerivativeOfCubicPolynomial(EstimateX)

#So to make this while loop safer we can make the variable DoRunning and MaxIterations
DoRunning = True
MaxIterations = 1000
Iterations = 0
EstimateX = 1

while DoRunning:
	if EstimateX < 0:
		DoRunning = False
	elif Iterations >= MaxIterations:
		DoRunning = False
	
	EstimateX -= CubicPolynomial(EstimateX)/DerivativeOfCubicPolynomial(EstimateX)

	Iterations += 1
