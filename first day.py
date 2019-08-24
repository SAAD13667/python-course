Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # The First Lesson
>>> print("Hello,World!")
Hello,World!
>>> exit()
>>> 
>>> if 5>2
SyntaxError: invalid syntax
>>> if 5>2;
SyntaxError: invalid syntax
>>> if 5 > 2:
	print("Five is greater than two")

	
Five is greater than two
>>> 
>>> # How to a void the mistake
>>> if 5>2:
print("5>2")
SyntaxError: expected an indented block
>>> # GOOD!!!
