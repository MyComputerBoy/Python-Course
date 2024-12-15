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

#Like by using append or pop
ListVariable.append("IDK & IDC")
ListVariable.pop(0)
#Note pop() uses the index for popping, meaning it can only pop items from indecies
#So using pop(0) will pop the first item, even if it contains a 0 in the list

#Dictionaries are a way to store items that you can refer to by "keys" and get the "items"
DictVariable: dict = {"Thomas": 25, "Dan": 19, "Asta": 23, "Alice": 11}

#You also use [] to acces items from a dict, but with dictionaries you can use the keys in smarter ways
print(DictVariable["Asta"])

#Like you can use a for statement to get both the keys and items as variables
for key, item in DictVariable:
	print("%s is %s years old" % (key, item))
#This will print the key (or in this case it can be seen as the name) is (the appropriate number) years old

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
	
	#The dunder str is a very useful function since it can be used to
	#Easily convert the class object to a string for easy to read info
	#In this example we create a string and puts the Real and Imaginary part
	#Into it using the %s's
	#This can just be called by calling str(The class object)
	def __str__(self) -> str:
		return ("%s + %si" % (self.Real, self.Imaginary))
