import math
#import numpy as np
#from array import *

from ScriptPull import *
arr = [1,2,3,4,5]
a = bsearch(arr,4)
b = clearall()
print(a,b)

# Categories: Basic, LL, BT, Graph, Math, Bits, Hash, Algo
# Basic = BasicDS, SearchSort, PrintIO, StackQueue
# Algo = Greedy, Divide&Conquer, Dynamic, 2pointer,

# -----------------------------------
# Basic: Given a list, print the # of numbers in the given range.
# Q: Sorted? --> no, Repetative? --> yes, Range is sorted? --> yes
arr = [10, 20, 30, 40, 50, 40, 40, 60, 70]
rng = [40, 60]

# Sol1: brute force
n = len(arr)
cnt = 0;
for i in range(n):
    print(i)
    if rng[0] <= arr[i] <= rng[1]:
        cnt = cnt + 1      
print(cnt)

# Sol2: single line
print(len( [ x for x in arr if rng[0] <= x <= rng[1] ] )) # note the [..]


# -----------------------------------
# Basic: Append at the beginning of arr
# Given:
arr1 = [10, 12, 13, 17]; arr2 = [40, 50];

# Sol1: slice
arr3 = arr1.copy()
arr3[:0] = arr2; print(arr3)

# Sol2:
arr2.extend(arr1); print(arr2)


# -----------------------------------



##-----------------------------------        
# BasicEasy 07: Find missing and additional values in arr1 wrt arr2
# Q:
# Given:
arr1 = [1, 2, 3, 4, 5, 6] 
arr2 = [4, 5, 6, 7, 8] 

# Sol: Use set diff
set1, set2 = set(arr1), set(arr2)
extra_at1 = list(set1.difference(set2))       # [1, 2, 3]
missing_at1 = list(set2.difference(set1))     # [7, 8]


##-----------------------------------
# BasicEasy 08: Multiply elements of int array with previous and next ones.
# Q: sorted? --> no,  
# Given: 
arr = [2, 3, 4, 5, 6]  # --> Output: 2*3, 2*4, 3*5, 4*6, 5*6
n = len(arr)

#Sol1: O(n), O(1)
arrm = []
for i in range(1, n-1):
  arrm.append(arr[i-1]*arr[i+1])
  
arr = [arr[0]*arr[1]] + arrm + [arr[n-2]*arr[n-1]]  
print(arrm)


##-----------------------------------        
# BasicEasy 09: Sort a List according to the length of the elements
# Q:
# Given:
arr = ['ab',(1,2,3), 'abcd', 'c']

# Sol 1: use sort()
arr.sort(key=len)       # in place
arr




##-----------------------------------
# BasicEasy 11: Print list after removing element at given index
# Q: none
# Given: 
arr = [1, 3, 2, 4, 5]
i = 3  # 4th no

# Sol:
arr.remove(arr[i])      # remove takes values, not index
print(arr)


##-----------------------------------
# BasicEasy 12: Get unique values from a list
# Q:
# Given: 
arr = [1, 3, 2, 3, 5]
n = len(arr) 

# Sol: Add/remove to a set, O(n) / O(n) --> no hashing needed
uniques = set()

for i in range(n):
    if arr[i] not in uniques:
        uniques.add(arr[i])
    else:
        uniques.remove(arr[i])   
    print(uniques)  


##-----------------------------------
# BasicEasy 13: Find Cumulative sum of a list
# Q:
# Given: 
arr = [10, 20, 30, 40, 50]   # --> Output : [10, 30, 60, 100, 150]
n = len(arr) 

# Sol:
summ = 0                    # need this var for the 1st calculation
csum = []
for i in range(0,n):
    summ = summ + arr[i]    # total sum so far
    csum.append(summ)    
print(csum)


##-----------------------------------        
# BasicEasy 14: Segregate (decompose) 0s and 1s within the array
# Q: 0s first? --> Y
# Given: 
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
n = len(arr)

# Sol: Use list comprehension
arr = [x for x in arr if x == 0] + [x for x in arr if x == 1] 
arr


##-----------------------------------        
# BasicEasy 15: Print unique rows in a given boolean matrix using Set with tuples
# Q: 
# Given: 
mat = [[0, 1, 0, 0, 1],
      [1, 0, 1, 1, 0],
      [0, 1, 0, 0, 1],
      [1, 1, 1, 0, 0]]
m = len(mat)
n = len(mat[1])

# Sol: conver to tuple and put it in set
myset = set()
for i in range(m):
    myset.add(tuple(mat[i]))
myset   
    

##-----------------------------------
# BasicEasy 16: Cyclically rotate an array by one
# Q:
# Given: 
arr = [1, 2, 3, 4, 5]   # o/p: [5, 1, 2, 3, 4]
n = len(arr)

# Sol: 
arr = [arr.pop()] + arr     # can only concat list + list 
print(arr)


##-----------------------------------
# BasicEasy 17: Get unique values from a list
# Q:
# Given:
arr = [10, 20, 10, 30, 40, 40]  # o/p: 10, 20, 30, 40
n = len(arr)

# Sol: Set
print(list(set(arr)))      # or, cast it to set and back to list 


##-----------------------------------
# BasicEasy 18: Check if a list is empty
# Q:
# Given: 
arr1 = []   # empty
arr2 = [2]  # not

# Sol:
if not arr1:    # or if len(arr1) == 0
  print("empty")
else:
  print("not-empty")


##-----------------------------------
# BasicEasy 19: Find common elements of 2 lists
# Q:
# Given:
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 6, 7, 8, 5, 4]
  
# Sol: Use set intersection
set1 = set(arr1)
set2 = set(arr2)
common = set1.intersection(set2)


##-----------------------------------
# BasicEasy 20: Check whether two lists are circularly identical
# Q:
# Given:
list1 = [10, 10, 0, 0, 10] 
list2 = [10, 10, 10, 0, 0]    # = are identical

# Sol: open one of the lists by doubling it, and map other list to it
map1 = map(str, 2*list1)
map2 = map(str, list2)
print(' '.join(map2) in ' '.join(map1) )  # 


##-----------------------------------
# BasicEasy 21: Count occurrences of an element in a Tuple
# Q:
# Given: 
tup = (1,2,1,1,5)           # round brackets to create
var = 1
n = len(tup)

# Sol:
cnt = 0
for i in range(n):
    if var == tup[i]:       # square brackets to access
        cnt += 1
cnt        


#-----------------------------------
# BasicEasy 22: Count the elements in a list until an element is a Tuple
# Q:
# Given: 
arr = [7, 8, (1, 3), (1, 4), 5]     # out = 2
n = len(arr)

# Sol:
cnt = 0
for i in range(n): 
    if type(arr[i]) == tuple:       # notice no " " 
        cnt += 1
cnt

 
#-----------------------------------
# BasicEasy 23: Iterate over multiple lists simultaneously
# Q: 
# Given:
arr1 = ['a', 'b']  # 
arr2 = [1, 2, 3]   # out = a 1, b 2


for (i, j) in zip(arr1, arr2):
     print(i, j)    # iterates 2 times since smallest array is size 2
    

##-----------------------------------        
# BasicEasy 24: Sort the values of first list using second list
# Q: 
# Given:
arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
arr2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# Sol: use Zip
zipped = zip(arr2, arr1)    # zipped pair
z = [x for _, x in sorted(zipped)] 
z

sea
##-----------------------------------
# BasicEasy 25: Count occurrences of an element in a list
# Q: 
# Given:
arr = [1, 2, 3, 2, 4, 2]      
x = 2

# Sol: use Counter
from collections import Counter 
cntr = Counter(arr) 
cntr[x]             # note square brackets
    

##-----------------------------------        
# BasicEasy 26: Creating a 3D matrix of zeros
# Q: 
# Given:   
m, n, o = 3, 2, 4
mat = [[ ['0' for i in range(m)] for j in range(n)] for k in range(o)] 
mat


##-----------------------------------        
# BasicEasy 27: Find the intersection of 2 lists
# Q: 
# Given:
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 6, 7, 1, 2, 2]  # out = [1, 2, 5]

# Sol 1: Use filtered list
arr3 = [x for x in arr1 if x in arr2]   

# Sol 2: Use set &
set1, set2 = set(arr1), set(arr2)
arr3 = list(set1 & set2)

# Mod: If sorted
arr1.sort()
arr2.sort()
# Sol 3: 



##-----------------------------------        
# BasicEasy 28: Convert an array to a list
# Q: 
# Given: 
array1 = np.array([1, 3, 5, 3, 3])

# Sol:
list1 = array1.tolist()     # direct conversion 


##-----------------------------------        
# BasicEasy 29: Make a string from a char arrayJ
# Q: 
# Given:
arr = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 
                        'm', 'i', 'n', 'g']
n = len(arr)

#Sol1:
string = ""
for ch in arr:
    string += ch
string

#Sol2: using join
string = ""
string = string.join(arr)   # joins with "" (no) separation


##-----------------------------------        
# BasicEasy 30: Print first m multiples of n without using any loop
# Q: 
# Given: 
n, m = 3, 4         # o/p = 3, 6, 9, 12

# Sol: Use range, O(n)
a = range(n, (m * n)+1, n)
print(*a)


#-----------------------------------
# BasicEasy 31: Multiply all numbers in the list (reduce)
# Q:
# Given:
arr = [1, 2, 3, 4]     # out = 24

# Sol:
from functools import reduce 
reduce((lambda x, y: x * y), arr)   # returns a list automatically


##-----------------------------------        
# BasicEasy 32: Split the Even and Odd elements into two different lists
# Q: 
# Given:
arr = [8, 12, 15, 9, 3, 11, 26, 23]
n = len(arr)

# Sol:
evens, odds = [], []
for i in range(n):
    if arr[i] % 2 == 0:
        evens.append(arr[i])
    else: # odd
        odds.append(arr[i])
evens
odds        


##-----------------------------------
# BasicEasy 33: Return the 1st recurring char in the string
# Q: 
# Given:
str = 'DBCABA'

# Sol:
ans = None
set1 = set()
for ch in str:              # <O(n)
    #print(ch, set1)
    if ch in set1:
        ans = ch
        break
    else:
        set1.add(ch)        # add is fast too but need mem reallocation
print(ans)


##-----------------------------------        
# BasicEasy 34: Largest, Smallest, Second Largest, Second Smallest in a List
# Sol: Sort and dump arr[0], arr[1], arr[len-1], arr[len-2]


##-----------------------------------        
# BasicEasy 35: Generate random numbers within a given range and store in a list
# Q: 
# Given:
num = 10
start, end = 20, 40

# Sol:
from random import random      # [0 1]
from random import randint     # [a b]

rand_nums = []
for i in range(num):
    rand_nums.append(randint(start, end))
rand_nums

##-----------------------------------
# BasicEasy 36: Find the min/max element’s position in a list
# Q: What to o/p if not enough elements? --> 0
# Given:
arr = [1, 0, 5, 3, 2]   # o/p = (1, 2)
n = len(arr)

# Sol: O(n)
pos_min = 0;
pos_max = 0;
for i in range(n):
    if arr[i] > arr[pos_max]:
        pos_max = i
    elif arr[i] < arr[pos_min]:
        pos_min = i
print(pos_min, pos_max)


# -----------------------------------
# BasicEasy 37: Union of two or more Lists
# Q: Order --> keep --> then ignore
   # Repetitions --> keep --> then ignore
# Given:
arr1 = [1, 2, 2, 3]
arr2 = [3, 4, 4, 5]

# Sol:
arr = arr1 + arr2   # maintains order
arr = list(set().union(set(arr1), set(arr2)))  # eliminates repetitions
print(arr)


# -----------------------------------
# BasicEasy 38: Print out the grade-school multiplication table up to 12x12
# Q: Space or tabs --> Tabs
# Given:
n = 12

# Sol:
for j in range(1,n+1):
    for i in range(1,n+1):
        print(i*j, end = "\t")
    print("")    


# -----------------------------------
# BasicEasy 39: Convert a list of Tuples into Dictionary
# Given:
tups = [('A', 1), ('B', 2), ('C', 3)]
n = len(tups)

# Sol:
d = dict()
for i in range(n) :
    d[tups[i][0]] = tups[i][1]
d


# -----------------------------------
# BasicEasy 40: Reverse an array in groups of given size
# Q: 
# Given:
arr = [1, 2, 3, 4, 5, 6, 7, 8] 
n = len(arr)
k = 3  # --> [3, 2, 1] + [6, 5, 4] + [8,7] = [3, 2, 1, 6, 5, 4, 8, 7]

# Sol: 
ch = 0  # chunk
j = 0
while ch*k < n : 
    if ch == 0 :    
        arr[ch*k:(ch+1)*k] = arr[(ch+1)*k-1: :-1]
    else :
        arr[ch*k:(ch+1)*k] = arr[(ch+1)*k-1 : ch*k-1 :-1]
    ch = ch + 1
arr        


# -----------------------------------
# Lambda: Sort a tuple by its float element in place
# Q: 
# Given:
t = [('1', '9.4'), ('2', '16.9'), ('3', '5.5'),  ('4', '4.2'), ('5', '7.3')]

# Sol: Use advanced sort w/ key + reverse
t.sort(key = lambda x: float(x[1]), reverse = True)
print(t)


# -----------------------------------
# Remove all characters in place other than alphabets
# Given:
mystr = "$Gee*k;s..fo, r'Ge^eks?"   # --> GeeksforGeeks

# Sol: Use ascii #
arr = list(mystr)
i = 0
while i < len(arr): 
    print(i, arr[i], ord(arr[i]))
    if  not (('A' < arr[i] < 'Z') or ('a' <  arr[i] < 'z')) :
        print('delete', arr[i])
        del arr[i]
    else :    
        i = i + 1
arr       


# -----------------------------------
# BasicEasy 44: Print anagrams together using List and Dict
# Given:
arr = ['cat', 'dog', 'tac', 'god', 'act']  # out = ['cat tac act dog god']
n = len(arr)

# Sol: O(n^logn)/O(n)
d = dict()   # d{sorted (unique) version: iter1, iter2 ... }
for i in range(n) :
    word = ''.join( sorted(arr[i]) )
    print(word)
    if word in d.keys() :    # if exists
        d[word] = ''.join( d[word] + ' ' + arr[i] )  
    else :
        d[word] = arr[i] 
#d
print(list(d.values()))


# -----------------------------------
# Remove all the consecutive duplicates in a string in place.
mystr = 'aabccccba'

# Sol1: Brute force array joining, O(n)/O(1)
i = 1
while i < len(mystr) :
    print(i, mystr)
    if mystr[i] == mystr[i-1] :
        mystr = mystr[ :i] + mystr[i+1: ]
        print("join")
    else :
        i = i + 1
mystr       # 4 array joins

# Sol2: Buffering to avoid duplicate comparisons, O(n)/O(1)
i = 1
temp = ''
while i < len(mystr) :
    print(i, mystr)
    if mystr[i] == mystr[i - 1]:
        if mystr[i] != temp:
            temp = mystr[i]
            mystr = mystr[ :i] + mystr[i+1: ]
            print("join")
        else :
            i = i + 1    
    else :
        i = i + 1
mystr       # 2 joins
   

# -----------------------------------
# Power of Two
x = 16                      # --> true

# Sol1: Log check, log2(2^n) = n = log2(16) = int?
def sol1(x):
    return math.log2(x) % 2 == 0
sol1(x)

# Sol2: Bits


# -----------------------------------
# Find Excel column number given the column name
ct = 'ABC'              # --> C*26^(3-1) + A*26^(2-1) + B^(1-1)

# Sol:
ord_A = ord('A')
LEN_ALPHA = 26
col = 0
for i in range(len(ct)):
    char = ct[i]    
    col += (ord(char) - ord_A + 1) * LEN_ALPHA ** (len(ct) - 1 - i)
    print(i, char, LEN_ALPHA ** (len(ct) - i - 1), col)
col


# -----------------------------------
# Find the smallest positive number missing from an unsorted array. Need O(n) / O(1)
arr = [2, 3, -7, 6, 8, 1, -10, 15];
n = len(arr)

#Sol1: Sort + Scan = O(nlogn + n) = O(nlogn)
#Sol2: Hash + scan = O(n)/O(n)
#Sol3: Utilize 0<= sol <=n, mark that element negative to denote presence
sol = 0
#j = 0
pos = 0
for i in range(n): 
    j = i + 1
    print(i, arr)
    while (arr[i] < 1) and (j < n):
        arr[i], arr[j] = arr[j], arr[i] 
        j = j + 1
    if (arr[i] >= 1) and ( arr[i] <= n):
        arr[arr[i]-1] = 0
        pos = pos + 1
arr


# -----------------------------------
# Find the max # of connected colors in 2D array
# - Write recursive DFS, hashtable --> what's your hashfunction? stack overflow?
# - push the neighbors in a stack as you visit them
mat = [[8, 8, 6, 7],
       [8, 6, 7, 6],
       [7, 6, 6, 6]]
m = len(mat); n = len(mat[0])       # 3x4

# Sol:
i, j = 0, 0
colors = dict()  # color: count

while (i <= 3) and (j <= 4):
    if mat[i, j] == mat[i + 1, j]:  # always inc: left to right, top to bottom
        colors[mat[i, j]] += 1  # update dict
        j
    if mat[i, j] == mat[i, j + 1]:
        colors[mat[i, j]] += 1  # update dict
    i = i + 1
    j = j + 1


# -----------------------------------
# String Compression
string = "aabcdecaaa"  # out = a2b1c5a3
n = len(string)

# Sol:
i = 0
cnt = 1
out = ''
while i < n:
    i += 1
    if i == n:  # last char
        out = out + string[i - 1] + str(cnt)  # dump

    elif string[i] == string[i - 1]:
        cnt += 1  #
    else:  # char change occured
        out = out + string[i - 1] + str(cnt)  # dump, O(n^2) op
        cnt = 1  # reset to 1 (not 0)
if len(out) > len(string):
    out = string
out


# -----------------------------------
# String Rotation
str1 = "abcde"
str2 = "deabc"  # out = true

# Sol:
len1, len2 = len(str1), len(str2)
out = False
str3 = 2 * str2  # str1 has to be a substring of str3
cnt, i, delay = 0, 0, 0
if (len1 == len2) and (len1 > 0):
    while (delay <= len1) and (i < len1):  # try to find a fixed delay like BER check, O(n1+n2)
        print(delay, i, cnt, str1[i], str3[i + delay])
        if str1[i] == str3[i + delay]:
            cnt += 1
            if cnt == len1:  # if enough count reached
                out = True  # quit
                break
            i += 1
        else:
            cnt = 0  # reset same char counter
            delay += 1  # try a different
out


##-----------------------------------
# Palindrome Permutation, O(n)/O(1)
string = "tacocat"
n = len(string)

hash_chars = 256 * [0]
char_delta = ord('a') - ord('A')  # fixed delta to handle case insensitivity
char_min = ord('A')
char_max = ord('z')
for i in range(n):
    if not (ord('A') < ord(string[i]) < ord('z')):  # if not letter
        out = False
    elif ord(string[i]) < ord('a'):
        hash_chars[ord(string[i]) + char_delta] += 1
    else:
        hash_chars[ord(string[i])] += 1
ch_odd = 0  # no need for evens
for j in range(256):
    if hash_chars[j] % 2 == 1:  # odd length --> need 1 single, (n-1)/2 twin chars
        ch_odd += 1
    # else:  # .. % 2 == 0 --> even
if (n % 2 == 0) and (ch_odd == 0):  # even length + no odds
    out = True
elif (n % 2 == 1) and (ch_odd == 1):
    out = True
else:
    out = False
out


# -----------------------------------
# Given a list of numbers, return all subsets of the list


# -----------------------------------
# Find a max and min in an array simultaneously
