# Contents: Assert, Try, Finally, Except, Speed (Timer, cProfile), Questions

for name in dir():
    if not name.startswith('_'):
        del globals()[name]

# Given to test
def fact(x):
    if x > 0:                   # ideally, x > 1
        return x * fact(x-1)
    else:  # base case
        return 1


# -----------------------------------
# Exceptions: try/except/finally/raise
# https://www.programiz.com/python-programming/exceptions
# https://www.tutorialspoint.com/python/python_exceptions.htm

assert fact(5 < 3, "5 is not smaller!")     # assertion error

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass


# -----------------------------------
# Speed:
import time
t1 = time.time()
# ---
fact(10)
# ---
t2 = time.time()
# ---
fact(30)
# ---
t3 = time.time()
te1  = t2 - t1              # time elapsed for first block
te2  = t3 - t2              #
print ("te1 = %.1f" % round(te1*1e6, 0), 'usecs')         # te1 = 7 usecs
print ("te2 = %.1f" % round(te2*1e6, 0), 'usecs')         # te2 = 12 usecs

import cProfile
cProfile.run('fact(30)')                    # = 34 func calls (4 primitive calls) in 0.001 secs


# -----------------------------------
# Space:
import sys
sys.getsizeof({'I':1, 'V':5})


# -----------------------------------
# QUESTIONS
# -----------------------------------
