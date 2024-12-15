"""VariableTypes.py -> This is a list of the different types of variables that python offers
"""

#Strings are for strings of text
StringVariable: str = "This is a string"

#Ints and floats are for numbers
IntVariable: int = 22						#Ints are whole numbers only
FloatVariable: float = 3.14159265358979		#Floats can have decimal parts too

#Booleans are true/false
BoolTrue: bool = True
BoolFalse: bool = False

#Lists are lists of anything that can be dynamically added to and removed from
ListVariable: list = [2.7182, 3, "String in list", False]

#You can also make your own 'type' by making classes and making them function with your own functionality
class Complex():
	#The __init__() function initialises the class with variables you can give it, like the Real and Imaginary variables given in this example
	def __init__(self, Real: float, Imaginary: float) -> None:	#The -> None part just shows what the function is expected to return
		self.Real = Real
		self.Imaginary = Imaginary
	
	#This function makes adding two Complex class objects able to be added together
	def __add__(self, other: "Complex") -> "Complex":
		return Complex(
			self.Real + other.Real, 
			self.Imaginary + other.Imaginary
		)
	
	#This function makes multiplying two Complex class objects able to be multiplied togerher
	def __mul__(self, other: "Complex") -> "Complex":
		return Complex(
			self.Real * other.Real - self.Imaginary * other.Imaginary, 
			self.Real * other.Imaginary + self.Imaginary * other.Real
		)


