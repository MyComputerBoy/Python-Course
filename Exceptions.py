"""Exceptions.py -> This is an introduction to exceptions in python
"""

#If you try to run code that should not work or is undefined in different ways it should raise an exception
#Like if you try to divide a number by zero it will raise the ZeroDivisionError exception
DivisionByZero = 25/0

#An exception cal also be risen by giving functions types they do not expect to be given
#Like giving the int() function a string that cannot meaningfully be converted to an int
ConvertionToIntError = int("Hello World!")

#There are a lot of things that can raise an exception, and in terminals they will most likely
#Show you which functions were called in which order and what went wrong in them

#But you can also raise an exception yourself if you know something is wrong
#For example if we make a function to divide two numbers and the denominator is zero
#We can raise the ZeroDivisionError ourselves by calling the raise statement
#We can also check the type of the input, and if it doesn't match anything we can
#Meaningfully process we can alsi raise the TypeError
def DivideNumbers(InputNumerator: float, InputDenominator) -> float:
	if InputDenominator == 0:
		raise ZeroDivisionError
	
	if InputNumerator is not float:
		raise TypeError
	if InputDenominator is not float:
		raise TypeError
	
	return InputNumerator/InputDenominator

#If we are unsure if something is gonna work, but wanna do different things if they do or don't
#We can use a try except statement
VariableA: float = 15
VariableB: float = 0

try:
	print(VariableA/VariableB)
except:
	print("We couldn't divide VariableA by VariableB, %s/%s" % (VariableA, VariableB))

#Note, just using an except: without specifying what exception we should expect is never a good idea
#Mostly because trying to close a program with [Ctrl]+[C] raises the KeyboardInterrupt exception
#Which WILL be caught by the except: statement and you won't be able to exit the program just by using [Ctrl]+[C]
#So the proper way to do this is by writing which exception we expect there to be risen
try:
	print(VariableA/VariableB)
except ZeroDivisionError:
	print("VariableB is zero, thus we can't divide them")