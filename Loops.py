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
