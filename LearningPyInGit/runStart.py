'''
author jean-thierry roy
date 2014-06-14
'''

from utilities.utils import *

#hello()

hello_class.i

# assign an imported class object to a
# then, of course, print a
a = hello_class.age
print 'a = hello_class.age : ', a

# assign __doc__ of class to b
# then print b
b = hello_class.__doc__
print 'b = hello_class.__doc__ : ', b

# Instance class to c
# then use instance to do some mods
# print the original class and the moded class instance
c = hello_class()
c.i += 4
print 'hello_class.i : ', hello_class.i, '\rc.i : ', c.i

# using the instanced class method (the def).
d = c.hello_w()
print 'd : ', d

# using a class with an __init__ method
# assign class argument
# print the class argument
e = init_class('Hello to world')
print 'e.data : ', e.data