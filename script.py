def sum(a,b):
	return a+b
def devide(a,b):
	if isinstance(a,str) or isinstance(b,str):
		raise ValueError("Строки делить нельзя")
	if b==0:
		raise ValueError("Cannot divide by zero")
	if isinstance(a,list) or isinstance(b,list):
		raise ValueError("Cannot divide lists")
	return a/b
def multilpy(a,b):
	return a*b


