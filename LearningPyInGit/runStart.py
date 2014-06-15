'''
author jean-thierry roy
date 2014-06-14
'''

from utilities.utils import hello_class

#hello()

hello_class.i

a = hello_class.age
print a

b = hello_class.__doc__
print b

c = hello_class()
c.i += 4
print hello_class.i, c.i 