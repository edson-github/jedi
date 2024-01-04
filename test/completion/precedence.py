"""
Test Jedi's operation understanding. Jedi should understand simple additions,
multiplications, etc.
"""
# -----------------
# numbers
# -----------------
x = [1, 'a', 1.0]

#? int() str() float()
x[12]

#? float()
x[1 + 1]

index = 0 + 1

#? str()
x[index]

#? int()
x[1 + (-1)]

def calculate(number):
    return number + constant

constant = 1

#? float()
x[calculate(1)]

def calculate(number):
    return number + constant

# -----------------
# strings
# -----------------

x = 'upp' + 'e'

#? str.upper
getattr(str, f'{x}r')

a = "a"*3
#? str()
a
a = 3 * "a"
#? str()
a

a = 3 * "a"
#? str()
a

#? int()
(3 ** 3)
#? int()
(3 ** 'a')
#? int()
(3 + 'a')
#? bool()
(3 == 'a')
#? bool()
(3 >= 'a')

class X():
    foo = 2
#? int()
(X.foo ** 3)

# -----------------
# assignments
# -----------------

x = [1, 'a', 1.0]

i = 0 + 1
i += 1
#? float()
x[i]

i = 1 + 1
i -= 3
i += 1
#? int()
x[i]

# -----------------
# in
# -----------------

a = 3 if 'X' in 'Y' else ''
# For now don't really check for truth values. So in should return both
# results.
#? str() int()
a

b = 3 if 'X' not in 'Y' else ''
# For now don't really check for truth values. So in should return both
# results.
#? str() int()
b

class FooBar(object):
    fuu = 0.1
    raboof = 'fourtytwo'

target = ''.join(['f', 'u', 'u'])
#? float()
getattr(FooBar, target)

target = u''.join(reversed(['f', 'o', 'o', 'b', 'a', 'r']))
#? str()
getattr(FooBar, target)


# -----------------
# repetition problems -> could be very slow and memory expensive - shouldn't
# be.
# -----------------

b = [str(1)]
l = list
for x in [l(0), l(1), l(2), l(3), l(4), l(5), l(6), l(7), l(8), l(9), l(10),
          l(11), l(12), l(13), l(14), l(15), l(16), l(17), l(18), l(19), l(20),
          l(21), l(22), l(23), l(24), l(25), l(26), l(27), l(28), l(29)]:
    b += x

#? str()
b[1]


# -----------------
# undefined names
# -----------------
a = f'{foobarbaz}hello'

#? int() float()
{'hello': 1, 'bar': 1.0}[a]

# -----------------
# stubs
# -----------------

from datetime import datetime, timedelta

#?
(datetime - timedelta)
#? datetime()
(datetime() - timedelta())
#? timedelta()
(datetime() - datetime())
#? timedelta()
(timedelta() - datetime())
#? timedelta()
(timedelta() - timedelta())

# -----------------
# magic methods
# -----------------

class C:
    def __sub__(self, other) -> int: ...
    def __radd__(self, other) -> float: ...

#? int()
(C() - object())
#? C() object()
(object() - C())
#? C() object()
(C() + object())
#? float()
(object() + C())
