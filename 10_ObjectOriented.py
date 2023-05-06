# Content: Class, Function, Partial Function, Operator Overload, Closures, Coroutines, Inheritance,
         # Global, Iterators, Generators, Decorators, Q

for name in dir():
    if not name.startswith('_'):
        del globals()[name]


# -----------------------------------
# Classes: Constructors runs first to init the object
class Gosu:
    """Class docstring."""
    skill = 1                           # default skill, class var (won't be seen by the methods)

    def __init__(self, skill):          # constructor, 1st arg is always 'self'
        """Function docstring."""
        self.name = "Alex"              # instance variable (object specific)
        self.skill = 5
        self.maxskill = 10              # hardcoded
        print('skill:' + str(self.skill))

    def __iter__(self):                 # returns an object that has __next__ method
        # self.skill = 6                # if we want to hardcore start
        return self

    def __next__(self):
        x = self.skill                  # store the current value
        if x >= self.maxskill:          # stop when it reaches limit
            raise StopIteration
            self.x = x + 1              # else, inc + return
            return x

    def outer(self, a=0, b=0, c=0):     # a,b,c are keywords (order flexibility), defaults are 0
        x = self.skill                  # func var = outer local var
        return x + a, x + b             # can return multiple var/sobjects as a tuple

# Usage: import Gosu --> lookup order: current dir > PYTHONPATH > default path
dir(Gosu)
help(Gosu)                              # access class docstring
Gosu.__doc__                            # access doc
obj1 = Gosu                             # notice no () used, constructor didn't run
Gosu.skill                              # = 1, class var access
obj1.skill                              # = 1, using default skill
obj1.name                               # = err, no default class var for name

obj2 = Gosu(5)                          # now skill is supplied, constructor ran
Gosu.skill                              # = 1, same, not relevant
[obj2.name, obj2.skill]                 # = ['Alex', 5]

obj2.outer(b=3, a=2)                    # = (5+2, 5+3) = (7, 8), accessing obj2 functions


# -----------------------------------
# Functions: = subroutine = procedure = subprocess
# Global: enables write permissions to upper level vars, need to be defined at each level
def outer1():
    a = 2
    print('a pre inner:', a)
    def inner():
        a = 3
        print('a at inner:', a)
    inner()
    print('a post inner:', a)
a = 5
outer1(); print('a outside:', a)        # = 2 3 2 5

def outer2():                           # using global/nonlocal
    a = 2
    print('a pre inner:', a)            # = 2
    def inner():
        global a                        # enables access to global only, not edit
        a = 3;                          # if didn't need to assign any, a would be 2
        print('a at inner:', a)         # but now it's 3
    inner()
    print('a post inner:', a)           # =2, because no global a in outer()
a = 5
outer2(); print('a outside:', a)        # 2, 3, 2, 3 --> inner() overwrote 5

# Nonlocal: doesn't write to top level, but at 1 level above only
def outer3():                           # using global/nonlocal
    a = 2
    print('a pre inner:', a)            # = 2
    def inner():
        nonlocal a                      # neither local nor global
        a = 3;                          # similarly, if not assigned, a would be 2
        print('a at inner:', a)         # = 3, overwrites at outer() level, but not at global level
    inner()
    print('a post inner:', a)           # =2, because no global a in outer()
a = 5
outer3(); print('a outside:', a)        # 2, 3, 3, 5


# -----------------------------------
# Packing:
lst1 = [1, 2, 3]
a, b, c = lst1                          # unpacks
lst2 = a, b, c                          # packs

# *args/**kwargs: used to pass varying number of args to a func, (kwarg = keyword + arg)
def fun(a, b, c, **kwargs):             # c = fun(a, b, c, d, e, f)
    total = a + b + c
    print(a, b, c, end=' ')             # 1 2 3
    for k, v in kwargs.items():         # print a packed dict arg
        print(v, end=' ')               # 4 5 6
        total = total + v
    return total
arg1 = 1;
args = [2, 3];                          # *args for (b, c), can also use tuple (2, 3)
kwargs = {'d':4, 'e':5, 'f':6}          # **kwargs for (d, e, f),
fun(arg1, *args, **kwargs)              # = 1 2 3 4 5 6 21
fun(arg1, *args, d=4, e=5, f=6)         # = 1 2 3 4 5 6 21


# -----------------------------------
# Partial func: creates a subset of another func, helps code reuse
from functools import partial
def adder(a, b, c):                     # general adder func
    return 100*a + 10*b + c
add_bc = partial(adder, 1,2)            # partial func with fixed a=1, b=2 (first items first)
print(add_bc(5))                        # = 100*1 + 10*2 + 5  = 125
add_ab = partial(add_abc, c=2)          # partial (sub) func with fixed c=2
print(add_ab(2, 3))                     # = 200*1 + 30*2 + 2  = 232, had to provide 2 args now


# Operator overload: creates a superset of another func, helps code reuse
def adder(a, b, c, d):                  # Python doesn't support overloading --> will overwrite
    pass                                # defines an empty function
del adder
def adder(*args):                       # workaround: add/concat manually using packing
    total = 0
    n = len(args)
    for i in range(n):
        if not isinstance(args[i], int):   # all items should be int o.w. can't add up
            return None
        total = total + args[i]*pow(10,n-i-1)  # = 1000*a + 100*b + 10*c + d
    return total
adder(1, 2, 3, 4)                       # = 1234


# -----------------------------------
# Generators: Func with yield, used for iterative algo that we only care about the next
def gen():
    yield 1
    yield 3
x = gen()                               # create a gen object and iterate
x.__next__()                            # = 1
x.__next__()                            # = 3
x.__next__()                            # StopIteration err

def fib(limit):                         # x = x-1 + x-2
    n1, n2 = 0, 1                       # init first 2 items
    while n1 < limit:
        yield n1
        n1, n2 = n2, n1 + n2            # w/o using a temp var
x = fib(5)                              # call it, a1 = 5 is the limit
print(list(x))


# -----------------------------------
# Decorators:
class Calculate:
    # @instancemethod                   # decorator not needed/accepted
    def add(self, x, y):                # must pass instance obj as the 1st param
        print(x + y)

    @classmethod                        # decorator needed, no onject needed to call
    def sub(cls, x, y):                 # must pass class obj as 1st param
        print(x - y)

    @staticmethod                       # decorator not needed
    def mul( x, y):                     # no obj needed for 1st param
        print(x*y)

    def div(x, y):                      # no decorator = static method
        print(x / y)

Calculate.add(2, 3)                     # = err, need to create the instance first to access
cal1 = Calculate()
cal1.add(2, 3)                          # = 5, now OK

Calculate.sub(2, 3)                     # = 2 - 3 = -1, can directly
cal1.sub(2, 3)                          # = -1, but works with instance too?

Calculate.mul(2, 3)                     # = 2*3 = 6, instance
Calculate.div(2, 4)                     # = 0.5,

# ---
def func1(func):
    func.data = func(3) + 2             #
    return func.data
# @func1                                # to specify the decorator to be applied on fun1
def func3(x3):
    return x3

func1(func3)                             # = 3+2 = 5


# -----------------------------------
# Closures: inner functions remember how their enclosing namespaces look like when they are defined
# - Enables the inner function see stuff beyond the outer function
# - object that remembers values even if they aren't in the memory
def func4():
    arr = [1]                           # mutable list
    def inner(x):                       # immutable str
        arr.extend([x])                 # compiler calls LOAD_DEREF, looks for the list ref only
        return l
    return inner

func4_in = func4()                      # points directly to the inner function (N/A yet)
func4_in(2)                             # = [1, 2]
print(f_inner(3))                       # = [1, 2, 3]

def func5():
    arr = [1]
    def inner(x):
        nonlocal arr      # to fix Unbound err, so the next line can use the global var above
        arr += [x]        # compiler calls LOAD_FAST to check list value --> UnboundLocalError
        return l
    return inner
func5_in = func5()
print(func5_in(2))
print(func5_in(3))


# - another ex:
x0 = 5                  # enables the inner function see stuff beyond the outer function
def fun1(x1):
    x1 = 2
    def fun2():       # won't see x0
        return x0 + x2
    return fun2         # we are not calling it but instead returning it

print(fun1(3))          # = 5 + 3 = 8
# fun2.__closure__      # screw it --> just write a class instad


# -----------------------------------
# Coroutine: generalization of subroutines, used for cooperative multitasking
# it can suspend and transfer (yield) control to other coroutine, then resume again
# just like OS switches between threads using scheduler, OOP language switch coroutines
# works like Generators in producing iterable data, but Coroutines can also consume data
# send() methods sends values to Coroutine, which sends back with (yield) expression

def print_name(prefix):     # advance execution to the first yield expression
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

        # calling coroutine, nothing will happen

corou = print_name("Dear")  # start sending input
corou.__next__()
corou.send("Atul")          # not in the name yielded
corou.send("Dear Atul")     # it's in the name --> it'll print the inputs so far
corou.close()               # generates GeneratorExit exception (can be catched)
corou.send("Atul")          #  //   StopIteration exception

# initial source(producer) starts the pipeline, sink ends it with possible data display/save
def producer(sentence, next_coroutine):     # split strings and feed it to pattern_filter
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None): # search for words ending with -ing
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:    # if pattern got matched, send it to next coroutine (print)
                next_coroutine.send(token)
    except GeneratorExit:           # catch exit exception and display
        print("Done with filtering!!")

def print_token():                  # sink, display the received tokens
    try:                            # i
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")

pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)  #
pf.__next__()
sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)                  # --> running, moving


# -----------------------------------
# Design Patterns
# 1) Singleton Class: Each class creates one unique object, creates issues during unit tests
class Singleton:
   __instance = None

   def __init__(self): # private constructor
      if Singleton.__instance != None:  # if an instance is already out, don't allow it
         raise Exception("This class is a singleton!")  
      else:
         Singleton.__instance = 1    # if not, keep creating the same instance
         
   @staticmethod        # static (common) access
   def getInstance():   
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance  
   @staticmethod 
   def printInstance():  
       print(Singleton.__instance)   
        
s1 = Singleton()
print(s1)
s1.printInstance()  # = 1

del s1
s1 = Singleton.getInstance()
print(s1)                # = 1, keeps creating the same object regardless of the object deletion

s2 = Singleton()        # exception --> can't create multi objects


# 2) Factory Class: classes print multiple objects (like a pencil)
class Factory:
   __instance = 0
   
   def __init__(self): # private constructor   
       if Factory.__instance != None:  # if an instance is already out
           Factory.__instance = Factory.__instance + 1 
       else:
           Factory.__instance = 1    # o.w. it's the 1st production
             
   @staticmethod     
   def getInstance():   
        if Factory.__instance == None:
            Factory()
        return Factory.__instance
   @staticmethod 
   def printInstance():  
       print(Factory.__instance)
            
f1 = Factory()  
print(f1)
f1.printInstance()      # = 1st product

f1 = Factory()
print(f1)               # different object this time
f1.printInstance()      # = 2nd product


# -----------------------------------
# QUESTIONS
# -----------------------------------
# ObjectOriented 01: Deck of Cards, how to subclass the DS to implement blackjack?
# Sol: 
class Deck:
    def Card(value, suit):
        c_value = value
        c_suit = suit
        
       
            