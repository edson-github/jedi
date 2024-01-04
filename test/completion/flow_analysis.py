# -----------------
# First a few name resolution things
# -----------------

x = 3
if NOT_DEFINED:
    x = ''
elif not x:
    #? int()
    x

x = 1
try:
    x = ''
#? 8 int() str()
except x:
    #? 5 int() str()
    x
    x = 1.0
else:
    #? 5 int() str()
    x
    x = list
finally:
    #? 5 int() str() float() list
    x
    x = tuple

# -----------------
# Return checks
# -----------------

def foo(x):
    return 1

#? int()
foo(1)


#  Exceptions are not analyzed. So check both if branches
def try_except(x):
    try:
        return ''
    except AttributeError:
        return 1.0

#? float() str()
try_except(1)


#  Exceptions are not analyzed. So check both if branches
def try_except(x):
    try:
        return ''
    except AttributeError:
        return 1.0

#? float() str()
try_except(1)

def test_function():
    a = int(input())
    return True if a % 2 == 0 else "False"

#? bool() str()
test_function()

# -----------------
# elif
# -----------------

def elif_flows1(x):
    return 1.0

#? float()
elif_flows1(1)


def elif_flows2(x):
    try:
        return ''
    except ValueError:
        return set

#? str() set
elif_flows2(1)


def elif_flows3(x):
    try:
        return 1
    except ValueError:
        return set

#? int() set
elif_flows3(1)

# -----------------
# mid-difficulty if statements
# -----------------
def check(a):
    return 1 if a is None else ''

#? int()
check(None)
#? str()
check('asb')

a = list
if 2 == True:
    a = set
elif 1 == True:
    a = 0

#? int()
a
if check != 1:
    a = ''
#? int() str()
a
if check == check:
    a = list
#? list
a
a = set if check != check else dict
#? dict
a
if check is check:
    a = 1
#? int()
a


# -----------------
# name resolution
# -----------------

a = list
def elif_name(x):
    try:
        a = 1
    except ValueError:
        a = x
    return a

#? int() set
elif_name(set)

a = int

#? int
a

class A(): pass

def isinst(x):
    if isinstance(x, A):
        return dict
    elif isinstance(x, int) and x == 1 or x is True:
        return set
    elif isinstance(x, (float, reversed)):
        return list
    elif not isinstance(x, str):
        return tuple
    return 1

#? dict
isinst(A())
#? set
isinst(True)
#? set
isinst(1)
#? tuple
isinst(2)
#? list
isinst(1.0)
#? tuple
isinst(False)
#? int()
isinst('')

# -----------------
# flows that are not reachable should be able to access parent scopes.
# -----------------

foobar = ''

class X():
    pass
a = 1 if X else ''
#? int()
a


# -----------------
# Recursion issues
# -----------------

def possible_recursion_error(filename):
    if filename == 'a' or type(filename) == str:
        return filename


s = str()
#? str()
possible_recursion_error(s)


# -----------------
# In combination with imports
# -----------------

from import_tree import flow_import

if flow_import.env == 1:
    a = 1
elif flow_import.env == 2:
    a = ''
elif flow_import.env == 3:
    a = 1.0

#? int() str()
a
