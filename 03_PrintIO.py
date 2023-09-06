# Contents: Printing, User input, File I/O, I/O module, PrettyPrint, Q

for name in dir():
    if not name.startswith('_'):
        del globals()[name]

# -----------------------------------
# Printing:
help('print')  # = print(value, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1, 2, 3, sep=' ', end='#')        # = 1 2 3#
print(lst = [1,2,3], end='#')           # = [1, 2, 3]#, container items default sep=' '
print('hi'*2)                           # = hihi = print('hi' + 'hi')

# formatting - %d/%i: signed, %u: unsigned, %X: hex_caps, %E: eform_caps, %G: float_short
print('{Who} <3 {food}'.format(food = 'chicken', Who = 'I'))  # = I <3 chicken
print("Formats: %c %s %d %u %f %x %X %e %g"
    % ('c', 'str', 10, 10, 10, 10, 10, 100.22456, 100.22456))
       # c str  10 10  10.000000 a A 1.002246e+02 100.225
print('%3.2f, %3.0f' % (5.256, 6.2))    # = 5.26, 6, %f: float

# escaping - common: \t, \n, \r, \u
print('He said \"hey\" \'look\'\fa')
print(r'C:\\Temp')                      # = C:\\Temp, rawstring to disable escaping
unicode = u"\u00dcnic\u00f6de"          # unicode for non ASCII support


# --Print_Advanced
# escaping - other: \a = Alert, \b = Backspace, \e = Esc, \cx = Control+X, \x = unicode Esc
from pprint import pprint               # to process inputs from other API
data1 = {'status': 'OK', 'results': [{'components': [{'long_name': 'Raj-path', 'types': ['route'],
         'short_name': 'Raj-path'}]}]}
print(data1)
pprint(data1)                           # more user friendly


# -----------------------------------
# User I/O: Read 2 ages from user (with a space separator) and print
a, b = [int(x) for x in input("Enter ages: ").split()]   # returns string, need to cast
print("Ages are %d, %d" % (a,b))        # = Ages are 4, 5

str = input("Enter your input: ")       # enter [x*5 for x in range(2,10,2)]
inp = eval(str); print(inp)             # [10, 20, 30, 40]

# File I/O: Read integers from a text file (one int per line), then add one in the end
# - open(file [, mode][, buffering]), 'r' = read, 'r+': read/write
import os
workdir = os.getcwd()
indir = '/data'
fname = 'integers.txt'
fpath = workdir + indir + '/' + fname
file = open(fpath, 'r+')                # to read + append, default: 'r'
file.mode                               # = 'r' = default access mode
file.name                               # ../Dropbox/GosuML/sw_python/data/integers.txt'
data = file.read()                      # read the whole thing
items = data.split()                    # ['1', '3', '4'], default: whitespace and newline

file.write('50')                        # writes at the end by default
file.tell()                             # we are at 13th char
file.seek(0)                            # return to the byte 0 (beginning)
file.readline()                         # = '10\n', line by line reading
file.seek(3)                            # = '\n',
file.readline()                         # = ' \n', every char is 2 byte --> hard to track
file.seek(2)                            # go back to empty 2nd line
file.write('\n20\n')                    # write there
file.close()                            # fhandle still exists but can't R/W anymore

file = open(fpath, 'r')
print(file.read().split())              # = ['10', '20', '30', '40', '50']
file.close(); del file                  # better to del handle too

import io                               # 2nd method
file = open(fpath, 'r')
data1 = file.readlines()
data1[1] = '20\n'
data1.append('50\n')
file = open(fpath, 'w')
file.writelines(data1)

file = open(fpath, 'r')
data2 = file.readlines()
print(data2)                            # = ['10', '20', '30', '40', '50']
file.close(); del file

import os
os.rename( "./data/integers.txt", "./data/numbers.txt")
os.remove("./data/numbers.txt")         # hope you saved it!


# -----------------------------------
# QUESTIONS
# -----------------------------------
# File I/O: Count the occurrences of each word in given text file using dictionary
fname = 'words.txt'
fpath = workdir + indir + '/' + fname
fhandle = open(fpath); data = fhandle.read()
import string
data = str(data)
for char in string.punctuation:
    data = data.replace(char, '')
words = data.lower().split()                # first lowercase, then split in a list
d = dict()
for w in words:
    d[w] = d.get(w,0) + 1                   # returns 0 if N/A
print(d)

# -----------------------------------
# Printing: Print a pyramid
n = 5                                           # let's say 5x5

# Sol:
for i in range(0, n):                           # rows
    for j in range(0, i + 1):                   # columns
        print("* ", end="")
    print("\r")                                 # return carriage, since 'i' is moving anyway

# Mod1: Rotate it 180 degrees
# Sol1:
for i in range(1, n+1):                         # for each row
    str = (n-i)*'  ' + i*' *'                   # 2 white spaces
    print(str)

# -----------------------------------
# Printing: Print a triangle (use same n)
# Sol:
import math
m = math.floor(n/2)
for i in range(1, n+1):                         # for each row
    str1 = (n-i)*' ' + i*'* '                   # 1 white space
    print(str1)

# -----------------------------------
# Printing: Print a number pattern (use same n)
# Sol:
str = ''
for i in range(1, n+1):                         # for each row
    str = str + " %s" % i                       # 1 white space
    print(str)

# Mod1: Make it continuous
# Sol1:
num = 1
for i in range(1, n+1):                         # for each row
    # num = 1                                   # solves previous example if defined here
    for j in range(0, i):
        print(num, end=" ")                     # 1 white space
        num = num + 1
    print("\r")                                 # return carriage for next row

# Mod2: Make it a char pattern
# Sol2:
c = 'A'
o = ord(c)                                      # get ASCII val for char c --> 65
for i in range(1, n+1):                         # for each row
    # o = ord(c)                                # solves previous example if defined here
    for j in range(0, i):
        print(chr(o), end=" ")                  # 1 white space
        o = o + 1
    print("\r")

# -----------------------------------
