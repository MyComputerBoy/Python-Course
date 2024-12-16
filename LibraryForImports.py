"""LibraryForImports.py -> A library for importing different functions for ease of use
"""

class Complex():
	def __init__(self, Real: float = 0, Imaginary: float = 0) -> None:
		self.Real = Real
		self.Imaginary = Imaginary
	
	def __add__(self, other: "Complex") -> "Complex":
		return Complex(
			self.Real + other.Real,
			self.Imaginary + other.Imaginary
		)
	
	def __mul__(self, other: "Complex") -> "Complex":
		return Complex(
			self.Real * other.Imaginary - self.Imaginary * other.Real,
			self.Real * other.Real + self.Imaginary * other.Imaginary
		)
	
	def __str__(self) -> str:
		return ("%s + %si" % (self.Real, self.Imaginary))
	
	def __repr__(self) -> str:
		return ("Complex(%s, %s)" % (self.Real, self.Imaginary))

class Maths():
	def __init__(self):
		self.TAU: float = 6.283185307179586476925286766559
		self.PI: float = 3.1415926535897932384626433832
		self.E: float = 2.718281828459045235360287471352

	def __IsNumber__(self, InputNumber) -> bool:
		IsInt = type(InputNumber) == int
		IsFloat = type(InputNumber) == float

		return (not IsInt) and (not IsFloat)

	def SquareRoot(self, InputNumber: float, Iterations: int = 100) -> float:
		#Newton's Method for calculating square root with Iterations number of Iterations
		#Starting Estimate
		Output: float = 1

		#Compute actual Newton's Method with Iterations iterations
		for i in range(Iterations):
			Output -= (Output ** 2 - InputNumber)/(2*Output)

		return Output

	def Exponent(self, InputNumber: float, Iterations: int = 10000) -> float:
		#Using the fact that e**x=(1+x/N)**N
		Output: float = (1+(InputNumber/Iterations))**Iterations

		return Output
	
	def NaturalLogarithm(self, InputNumber: float, Iterations: int = 1000) -> float:
		#Using the Taylor Serie's of the ln(1+x)=x-x**2/2...

		Estimate: float = 1
		for i in range(Iterations):
			Exponentiated: float = Maths.Exponent(Maths, Estimate)
			Estimate -= (Exponentiated-InputNumber)/Exponentiated
		
		return Estimate

	def Faculty(self, InputNumber: int) -> int:
		Output: int = 1
		for i in range(1, InputNumber+1):
			Output *= i
		return Output

	def Sinus(self, InputNumber: float, Iterations: int = 100) -> float:
		#Using the Taylor Serie's for sinus sin(x)=x-x**3/3!+x**5/5!
		Output: float = 0
		for i in range(1, Iterations):
			Sign = (-1)**(i-1)
			Numerator = InputNumber**(2*i-1)
			Denominator = Maths.Faculty(Maths, 2*i-1)

			#(+ or -)x**(2i+1)/(2i+1)!
			Output += Sign * Numerator/Denominator
		return Output
