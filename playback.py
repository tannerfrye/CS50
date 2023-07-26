

import re
#prompt what to say
x = input("What would you like to say? ")

#change the input to have 3 periods between words
y = re.sub("\s", "...", x)

#sub is a method from the re module

#print the output
print(y)
