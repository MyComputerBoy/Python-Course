"""Conditions.poy -> An introduction to conditions in python
"""

#This is just some setup for the different examples
VariableA: str = "Alice"
VariableB: str = "Bob"
VariableC: int = 2
VariableD: int = 3

#The most basic condition in python is the if statement
#If statements can check wether somethings are equal or greater than or the likes
#In this case we'll check if VariableA is equal to VariableB
#Note the two equal characters, since a single equal character defines a variable
#We need to to check equality
if VariableA == VariableB:
	print("VariableA is indeed equal to VariableB.")

#We can also check if they aren't equal
if VariableA != VariableB:
	print("No, VariableA is not equal to VariableB.")

#We can even chain multiple conditions together to check different statements after each other
#And if none of them are met, we can use the else statement to handle the conditions even if none of them are met
if VariableC > VariableD:
	print("VariableC is definitely greater than VariabeleD.")
elif VariableC == VariableD:
	print("Yes, VariableC is absolutely equal to VariableD.")
elif VariableC < VariableD:
	print("No, VariableC is less than VariableD.")
else:
	print("We don't know about the conditions.")

#We can even check what type a variable is by the is operator
if VariableA is str:
	print("VariableA is definitely a string type.")
elif VariableA is int:
	print("No, VariableA is actually an integer.")
