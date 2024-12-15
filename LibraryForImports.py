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
		pass

	def SquareRoot(InputNumber: float, Iterations: int = 100) -> float:
		#Newton's Method for calculating square root with Iterations number of Iterations
		#Starting Estimate
		Output: float = 1

		#Compute actual Newton's Method with Iterations iterations
		for i in range(Iterations):
			Output -= (InputNumber - Output ** 2)/(2*Output)

		return Output

	def Exponent(InputNumber: float, Iterations: int = 100) -> float:
		#Using the fact that e**x=(1+x/N)**N
		Output: float = 1+(InputNumber/Iterations)**Iterations

		return Output
	
	def NaturalLogarithm(InputNumber: float, Iterations: int = 100) -> float:
		#Using the Taylor Serie's of the ln(1+x)=x-x**2/2...
		InputNumber -= 1

		Output: float = 0
		for i in range(Iterations):
			Sign = (-1)**i
			Numerator = InputNumber ** i
			Denominator = i

			#(+ or -)x**i/i
			Output += Sign * Numerator/Denominator
		
		return Output

	def Faculty(InputNumber: int) -> int:
		Output: int = 1
		for i in range(InputNumber):
			Output *= i
		return Output

	def Sinus(InputNumber: float, Iterations: int = 100) -> float:
		#Using the Taylor Serie's for sinus sin(x)=x-x**3/3!+x**5/5!
		Output: float = 0
		for i in range(Iterations):
			Sign = (-1)**i
			Numerator = InputNumber**(2*i+1)
			Denominator = Maths.Faculty(2*i+1)

			#(+ or -)x**(2i+1)/(2i+1)!
			Output += Sign * Numerator/Denominator
		return Output
