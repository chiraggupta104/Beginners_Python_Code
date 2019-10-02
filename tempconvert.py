def fToC():
	F = int(input("Enter temp in Fahrenheit: "))
	C = (F - 32) * 5.0/9.0
	print(str(F) + " Fahrenheit is " + str(C) + " in Celsius\n")

def cToF():
	C = int(input("Enter temp in Celsius: "))
	F = 9.0/5.0 * C + 32
	print(str(C) + " Celsius is " + str(F) + " in Fahrenheit\n")

option = int(input("Choose an option: \n (1) Fahrenheit to Celsius \n (2) Celsius to Fahrenheit \n :::"))
if(option == 1):
	fToC()
if(option == 0):
	cToF()
