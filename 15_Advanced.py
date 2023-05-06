# Contents: Map/Reduce, Struct, List mutation, Set override, Itertools, Fraction,
          # RegularExp, Date/Calendar/Time, Keyword

for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# -----------------------------------
# Map: https://book.pythontips.com/en/latest/map_filter.html
def square(x):
    return x**2
sq = map(square, range(5))              # applies a function to every member of iterable
print(list(sq))                         # = [0, 1, 4, 9, 16]

# Reduce:
import functools
arr = [1, 3, 5, 6, 2]
# reduce(fun, seq) --> apply fun to all sequence elements
sum1 = functools.reduce(lambda a,b: a+b, arr)  # (n1 + n2)+  n3 ... = 17
import operator
sum2 = functools.reduce(operator.add, arr)     # avoid lambda using op --> more readable!
# accumulate(seq, fun) --> opposite syntax, also returns the intermediate elements too
import itertools
sum3 = itertools.accumulate(arr, lambda a,b : a+b)  # [n1 n1+n2 n1+n2+n3 ..] = [1, 4, 9, 15, 17]
print(sum1, sum2, list(sum3))    # last element of accu = reduce()


# -----------------------------------
# Struct:
import struct                       # C structs represented as Python bytes objects
# struct.pack(format, v1, v2, ...)  # format strings specify the expected layout when
# packing/unpacking
var = struct.pack('hhl',1,2,3) # h/l is long/short in C, so hhl is short/short/long
print(var)
var = struct.pack('iii',1,2,3) # 8 bit per integer --> all long
print(var)


# -----------------------------------
# List mutation
a = [1,2]; b = [3]
arr = [a, b]
b.append(4); print(arr)                 # = [[1, 2], [3, 4]], dynamically modifies

# Set override
def f(x, s=set()):
    s.add(x)
    print(s)
f(1)                    # = {1}, s=set() is evaluated once, but nothing given
f(4)                    # = {1, 4}, s is mutable, not constructed again
f(1, {2, 3})            # = {1, 2, 3}, {2, 3} overrides the set() init, constructing another copy
f(5)                    # = {1, 4, 5}, continue with the original construction


# -----------------------------------
# Itertools: Used for speed, list, tuple, set, string, dict are all built-in iters
import itertools
import operator
# method(iter, func)                            # execute function for each, default is addition
lis = [1, 2, 3]                                 #
lis1 = list(itertools.accumulate(lis))          # = 1, 1+2, 1+2+3 = [1, 3, 6]
lis2 = list(itertools.accumulate(lis, operator.mul))  # = [1, 2, 6]
print(list(itertools.chain(lis1, lis2)))        # chain = print together
list(itertools.compress(lis1, [1, 0, 1, 1]))    # = [1, 6], filtering with boolean list
print(list(itertools.dropwhile(lambda x : x > 3, lis1)))  # prints after the func returns false
print (list(itertools.takewhile(lambda x :  x <= 2,lis1 )))  # opposite, prints till // // //
print(list(itertools.filterfalse(lambda x : x <= 2, lis1)))  # = [3, 4], prints when it's false
print(list(itertools.islice(lis1, 1, 4, 2)))    # selective print (start, stop, step) --> [2 4]
print (list(itertools.starmap(min,lis1)))       #
print(list(itertools.product('AB', '12')))      # cartesian product
print(list(itertools.permutations('ABC',2)))    # all possible permutations of size n
print(list(itertools.repeat(25,4)))             # repeats n times --> 25 25 25 25
print(list(iterator.count(5, 2)))               # infinite iter: start, step --> 5,7,9,11.. (error)
print(list(iterator.cycle([1,2,3,4])))          # // but cyclic --> 1 2 3 4 1 2 3 4 .. (error)


# -----------------------------------
# Date/Calendar
import time as tm                       # alternatively: from timer import default_timer
from datetime import date
ticks = tm.time();                      # secs since epoch(Jan 1st 1970)
date.fromtimestamp(ticks)           # calculate date from seconds

tm.asctime(tm.gmtime(ticks))            # = 'Thu Jul 21 19:19:01 2022, 24char readable format
tm.ctime(ticks)                         # = 'Thu Jul 21 19:19:01 2022', same thing in local time
tm.localtime()                          # returns tuple of everything:  tm_year=2022, tm_mon=7,
# tm_mday=21, tm_hour=20, tm_min=13, tm_sec=1, tm_wday=3, tm_yday=202, tm_isdst=0
# tm.tzset()                            # sets timezone for libs, dangerous
tm.timezone
tm.sleep(5)                             # suspends the calling thread for n secs
[date.min, date.max]                    # = 0001-01-01 9999-12-31, timer can work till 2038
date(1997,4,1)                          # = 1997-04-01, prints given Y/M/D in yyyy-mm-dd)
date.today()                            # get current date
date.today().day                        # = 22

import calendar as cal
cal.calendar(2022,2,1,6)                # syntax: (year, width, spacing, col seperators)
cal.month(2022,9,4,1)                   # syntax: (year, month, width, spacing)
cal.firstweekday()                      # = 0, (Monday, by default) --> can setfirstweekday(n)
cal.isleap(2022)                        # = False, year with short (29day) Feb
cal.leapdays(2022, 2030)                # = 2
cal.weekday(2022,7, 21)                 # = 3 (Thu)
cal.monthcalendar(2022,9)               # = [[0, 0, 0, 1, 2, 3, 4], [5, 6, ...
cal.monthrange(2022,9)                  # = (3, 30), returns tuple

# Time:
from datetime import time
print(time())                           # = 00:00:00
print(time(18, 6, 15))                  # = 18:06:15, leading zeros  not permitted

from datetime import datetime as dt
dt1 = dt(2017, 11, 28, 23, 0, 0)        # = 2017-11-28 23:00:05, when printed
dt2 = dt(2022, 8, 22, 0, 30, 0)         # = 2017-11-28 23:00:05, //
delta_dt = dt2 - dt1                    # becomes a timedelta object
print(delta_dt, type(delta_dt))         # = 1727 days, 1:30:00 <class 'datetime.timedelta'>
delta_dt.total_seconds()                # = 149218200.0

dt2f = dt2.strftime("%d/%m/%Y, %H:%M:%S")  # = '22/08/2022, 00:30:00', to str, order changed
dt2 = dt.strptime('22/08/2022', "%d/%m/%Y") #  = create dt object from str
print(dt2)                              # = 2022-08-22 00:00:00

# import pytz                           # need to import to handle time zones
# dt_Local = dt.now()                   # local dt object
# tz_London = pytz.timezone('Europe/London')
# dt_London = dt.now(tz_London)         # London dt object


# -----------------------------------
# Regular Expressions
# seeks pattern in the string with flag modifiers set by bitswise OR (|)
# returns None if no match, returns group() if match
# raises the exception re.error
# Syntax: re.match(pattern, string, flags=0)
# re.I = case-insensitive
# re.M = Makes ^/$ match the start/start of the line instead of the string
# re.S = Makes a period (dot) match any character, including a newline.
# Control chars: (+ ? . * ^ $ ( ) [ ] { } | \) --> can be escaped with a "\"
# []    : char class
# ^/$   : matches beginning vs end
# +/*   : >=1 vs any occurrences
# .     : matches any character except newline
# ?     : matches 0 vs 1 occurrences
# |     : matches with any of the characters separated by it
# \d \D : matches any digit vs non-digit
# \s \S : matches any space vs non-space (tabs are different)
# \w \W : matches any alphanumeric vs non-alphanumeric
import re
p = re.compile('[a-e]')         # creates regular expression of char class [a-e] --> [a,b,c,d, e]
print(p.findall("AfedcBa"))     # = [e, d, c, a], case sensitive
str1 = "I went to him at 11 A.M. on 4th July 1886"
p = re.compile('\d')            # decimal RE class [0-9]
print(p.findall(str1))           # = [1, 1, 4, 1, 8, 8, 6]
p= re.compile('\d+')            # same but in groups of +=1
print(p.findall(str1))           # = ['11', '4', '1886'] --> good to extact meta data over internet

print(re.split('\W+', str1))     # = [.. 'him', 'at', '11', 'A', 'M', 'on', '4th', 'July', '1886']
# re.match(pattern, string, flags=0)    # matches a pattern to a whole string

line = "Cats are smarter than dogs"
match1 = re.match( r'cats', line, re.M|re.I)    # checks at the beginning
print(match1.group())
match2 = re.match( r'dogs', line, re.M|re.I)    # check at the beginning
#print(match2.group())                 # no match since dogs is at the end

search1 = re.search( r'dogs', line, re.M|re.I)  # searches through all
print(search1.group())
search2 = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
print(search2.group() + " / " + search1.group(1) + " / " + search1.group(2))

# re.sub(pattern, repl, string, max=0)    # replace pattern with repl
phone = "2004-959-559 # This is Phone Number"
num = re.sub(r'#.*$', "", phone)    # . = match all chars, $ = new line,
print(num)                          # comments deleted
num = re.sub(r'\D', "", phone)      # \D = match nondigits
print(num)                          # dashes removed


# -----------------------------------
# Others:
import keyword                          # keyword module
keyword.iskeyword('yield')


# -----------------------------------
# QUESTIONS
# -----------------------------------
# Lambda: Reverse sort (in place) tuples by its 2nd float element
t = [('1', '9.4'), ('2', '16.9'), ('3', '5.5'),  ('4', '4.2'), ('5', '7.3')]

# Sol: Use advanced sort w/ key + reverse
t.sort(key = lambda x: float(x[1]), reverse = True)
print(t)

# -----------------------------------

