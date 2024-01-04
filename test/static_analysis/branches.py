# -----------------
# Simple tests
# -----------------

import random

x = '' if random.choice([0, 1]) else 1
y = '' if random.choice([0, 1]) else 1
x.upper()
# This operation is wrong, because the types could be different.
#! 6 type-error-operation
z = x + y
z = x + y


# TODO enable this one.
#x = 3
#if x != 1:
#    x.upper()

# -----------------
# With a function
# -----------------

def addition(a, b):
    # Might still be a type error, we might want to change this in the
    # future.
    #! 9 type-error-operation
    return a + b

addition(1, 1)
addition(1.0, '')
