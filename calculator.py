# Калькулятор

from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.BLACK )
print( Back.WHITE )

what = input( "Какую операцию выполняем? (+, -, *, /, //, %, **): " )

print( Back.BLUE )

a = float( input("Введите первое число: ") )
b = float( input("Введите второе число: ") )

print( Back.RED )

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
elif what == "*":
	c = a * b
	print("Результат: " + str(c))
elif what == "/":
	c = a / b
	print("Результат: " + str(c))
elif what == "//":
	c = a // b
	print("Результат: " + str(c))
elif what == "%":
	c = a % b
	print("Результат: " + str(c))
elif what == "**":
	c = a ** b
	print("Результат: " + str(c))		
else:
	print("Выбрана некорректная операция!")

