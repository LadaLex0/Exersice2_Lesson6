x = input('Write your name: ')
import re
x1 = re.sub("[0-9]", "", x)
x2= x1.title ()
print(x2)