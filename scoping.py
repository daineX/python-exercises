"""
Exercise about scoping rules in Python (2).
What do all the print statements display?
In case one of them produces an exception, what needs to be changed in order
for it to display something?
"""
x = 1
def foo_x():
    x = 3
foo_x()
#print x

y = 1
def foo_y():
    global y
    y = 3
foo_y()
#print y

t = 3
def foo_t(t):
    return t
#print t
#print foo_t(4)

z = 3
def foo_z(some_number):
    some_number = some_number + 1
foo_z(z)
#print z

d = {}
def foo_d(some_dictionary):
    some_dictionary['foo'] = 1
foo_d(d)
#print d


def power(base, exp):

    def power_up(current):
        return current * base

    n = base
    for i in xrange(exp - 1):
        n = power_up(n)
    return n

#print power(10, 3)
#print powerup(30)

def class_maker(base, add_op):

    class Foo(base):
        def __add__(self, other):
            return add_op(self, other)
    return Foo

y = 80
WeirdInt = class_maker(int, lambda x, y: x * y)
w = WeirdInt(3)
#print w + 2


for i in range(10):
    if i > 5:
        break
#print i

class Foobar(object):

    def __init__(self, bar):
        self.bar = bar

    def eggs(self):
        return bar

f = Foobar(3)
#print f.eggs()

class CoolBar(object):

    drinks = 30

    def eggs(self):
        return drinks

c = CoolBar()
#c.eggs()

class ToolBar(object):

    drinks = 30

    def set_drinks(self, d):
        self.drinks = d

    def eggs(self):
        return self.drinks

    @classmethod
    def classy_eggs(cls):
        return cls.drinks

    @classmethod
    def set_classy_eggs(cls, d):
        cls.drinks = d

t = ToolBar()
#print t.eggs()
t.set_drinks(10)
#print t.eggs()
#print t.classy_eggs()

t.set_classy_eggs(60)

t2 = ToolBar()
#print t2.classy_eggs()
#print t2.eggs()
