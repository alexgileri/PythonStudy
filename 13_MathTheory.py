# Contents: Algebra, Random, Trigonometry, Random, MatrixOps, Questions

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var
import math                             # casts to and returns float
# from math import sqrt                 # sub-import ex
# del sqrt                              # delete the sub-method


# -----------------------------------
# Algebra
a = 3.4536
max(2, 3, 1)                            # = 3, doesn't need math module
round(-1.5)                             # = -2, rounds away from the zero
round(a, 2)                             # do= 3.45, rounds at n-digits away from t
abs(-3.5)                               # = 3.5
math.ceil(a)                            # = 4
math.sqrt(16)                           # = 4.0
dir(math.sqrt)                          # all var/func in a module as sorted list of strings
print('%.2f' % a)                        # = 3.45, setting precision
print("{0:.2f}".format(a))              # = 3.45, 2nd method
math.ceil(-3.5)                         # = -3
math.floor(-3.5)                        # = -4
math.pow(2, 5)                          # = 2**5 = 32.0
math.exp(1)                             # = e^1 = 2.718..
print(math.e)                           # same thing except more explicit
math.log(math.exp(2))                   # ln(e^2) = 2
math.log(100, 10)                       # = log10(100) = 2
math.log10(100)                         # alternative --> better
math.pow(3,2)                           # = 3**2 = 9
math.trunc(a)                           # = 3, removes the decimal part
math.factorial(4)                       # = 2*3*4 = 24
math.copysign(2, -5)                    # returns 1st var with the sign of 2nd var --> -2
math.gcd(30, 18)                        # = 6, greatest common divisor (no LCM)
math.isnan(math.nan)                    # = True
math.isinf(math.inf)                    # = True
math.isfinite(math.inf)                 # = False, NaN and Inf aren't finite


# -----------------------------------
# Random
import random                           # no need to import math
arr1 = [0, 1, 2, 3]
random.randint(0, 5)                    # random integer in [0 5] --> default range is [0 1]
random.seed([2])                        # need to use this before random() calls
random.random()                         # %1.16f floating point [0 1] (useless if called after seed)
random.choice(arr1)                     # returns a random item from a container
random.randrange(0, 10, 2)              # [0 10), inc2 --> 0,2,4,6,8 (step should be integer)
random.uniform(0, 10)                   # this is what you need for float generation
random.shuffle(arr1)                    # shuffles the container, returns None
print(arr1)


# -----------------------------------
# Trigonometry
import cmath                            # complex math
math.degrees(math.pi)                   # = 180.0
math.radians(45)/math.pi                # = 0.25pi/pi = 1/4
math.sin(math.pi/2)                     # = sin(90) = 1 --> similarly sinh(), asinh(h)
math.atan(1)/math.pi                    # = 45/180 = 1/4
math.atan2(2, 4)                        # = atan(y/x)
z = 1 + 2j                              #
cmath.phase(z)                          # = 1.107.. rads
cmath.sqrt(-4)                          # = 2j, can't use math.sqrt

# -----------------------------------
# Operator: assignment and computation together --> use for mutable containers only
import operator
# for vars
a, b = 7, 3                             # multivar decleration
operator.iadd(a, b)                     # a = a + b
operator.floordiv(a, b)                 # = 2, others: sub/mul, pow, truediv, floordiv(=mod)
operator.lt(a, b)                       # = a =< b = False, others: gte, gt, eq/neq
operator.iconcat('b', 'c')              # = 'bc'
# for bits
operator.and_(0, 1)                     # = False, others: or_, xor, invert
x = operator.rshift(8,2)                # = 1000>>2 = 0010 = 2, bit-wise right shift
# for arrays
arr1 = [1, 2, 3]; arr2 = [3, 4, 5]
operator.add(arr1, arr2)                # arr1 stays, result is [1, 2, 3, 3, 4, 5]
operator.concat(arr1,arr2)              # same //
operator.iadd(arr1, arr2)               # i.. means a+=b op, so arr1 mutates to //
operator.getitem(arr1,5)                # get the last element --> 5
operator.setitem(arr1, slice(1, 3), [8, 9])  # set  to 4 --> [1, 8, 9, 3, 4, 5]
operator.delitem(arr1,1)                # delete the 2nd --> [1, 9, 3, 4, 5]
operator.contains(arr2,4)               # True


# -----------------------------------
# MatrixOps:
mat1 = [[1,2], [3,4], [5,6]]            # m[1] = [3,4]
print(mat1[0][1])                       # 1st row, 2nd col = 2
m = len(mat1); n = len(mat1[0])

for row in mat1:                        # prints each row
    print(row)

# Transpose
mat1_t = [[mat1[j][i] for j in range(m)] for i in range(n)]
for row in mat1_t:
    print(row)
print()

mat1_zip = zip(*mat1)                   # using Zip
for row in mat1_zip:
    print(row)

import numpy as np
np.transpose(mat1)                      # using Numpy


# -----------------------------------
# Combinatorics:
# n digits --> 10^(n-1) representation

# -----------------------------------
# QUESTIONS
# -----------------------------------
# Math: Swap 2 integers without a temp variable
# Given:
a, b = 2, 3

# Sol1:
a,b = b,a; print(a, b)

# Sol2: cool
a = a + b           # set a to sum
b = a - b           # = a + b - b = a
a = a - b           # = a + b - a = b
print(a, b)

# -----------------------------------
# Math: