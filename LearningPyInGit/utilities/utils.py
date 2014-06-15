'''
author jean-thierry roy
date 2014-06-14
'''


def hello():
    print 'hello world'
    
class hello_class:
    """A very simple class in py."""
    i = 123456
    name = 'john'
    age = 46
    def hello_w(self):
        return 'Hello world'

class init_class:
    """A class with an __init__"""
    def __init__(self, string):
        self.data = string