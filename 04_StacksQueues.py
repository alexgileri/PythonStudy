# Contents: Stack Construction/Ops, Queue Construction/Ops, Q

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var


# -----------------------------------
# Stacks (LIFO)                        # O(1) insert/remove, O(n) access (same as arrays)
stack = [1, 2, 3]
stack.pop()                             # = [1, 2]
stack.append('a')                       # = [1, 2, 'a']

class Stack:
    def __init__(self):
        self.arr = []
    def isEmpty(self):
        return self.arr == []

    def push(self, x):
        self.arr.append(x)
    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.arr.pop()

    def peek(self):
        return self.arr[-1]
    def print(self):
        return self.arr
    def size(self):
        return len(self.arr)
    
    def min(s):
        if s.isEmpty() == []:
            return -1
        minn = s.pop()
        for i in range(s.size()):
            x = s.pop()
            if x < minn:
                minn = x
        return minn

s = Stack()
s.push(3); s.push(4); s.push(1); s.push(2)
s.print()                               # = [3, 4, 1, 2]
print(s.size(), s.peek(), s.min())      # = 4, 2, 1


# -----------------------------------
# Queue: (FIFO, O(n) access still but a little slower during removal (shifting)
from collections import deque           # so employ deque that can do fast ops from start/end
queue = deque([1, 2, 3])                # = ([1, 2, 3]) --> deque object
queue.append(4)                         # = ([1, 2, 3, 4])
queue.popleft()                         # = 1, queue = ([2, 3, 4])


# -----------------------------------
# QUESTIONS
# -----------------------------------
# StackQueue 01: Sort Stack s.t. smallest items are on the top
# Q: Can use additional stack? --> yes but not array
# Given: s = [2, 1, 4, 3] --> [4, 3, 2, 1] 

# Sol: O(n^2)/O(n)
def s_sort(s):          
    #n = s.size()               
    r = Stack()         # result stack             
    while not s.isEmpty() : 
        tmp = s.pop() 
        while (not r.isEmpty()) and (r.peek() > tmp) :  # if can't reach smaller elements yet
            s.push(r.pop());   # keep pouring over the s                    
        r.push(tmp)         # when done, insert the next min to r
        # max element in s and will be inserted in r too in the end
    while not r.isEmpty() :     # now r is sorted but in descending order
        s.push(r.pop())         # so pour r back to s                 
s_sort(s)
s.print()                   # done

# Sol:
from queue import Queue
qq1 = Queue()
qq2 = Queue()
def sq_push(q1, q2, x):
    q2.put(x)
    while not q1.empty() :
        q2.put(q1.queue[0])
        q1.get()    # no return for push
    qtemp = q1      # 
    q1 = q2
    q2 = qtemp
    
def sq_pop(q):
    return q.get()

def sq_print(q1, q2):
    arr1, arr2 = [], []
    for i in range(q1.qsize()):
        arr1.append(q1.get())
        arr2.append(q2.get())
    return arr1, arr2

sq_push(qq1, qq2, 'a')
sq_push(qq1, qq2, 'b')
sq_push(qq1, qq2, 'c')

sq_print(qq1, qq2)

sq_pop(q1)


# -----------------------------------
# StackQueue 05: Animal Shelter
# FIFO basis, people select cat/dog but have to adopt the oldest
# Sol:
class Animal:
     def __init__(self):
         self.dogs = []
         self.cats = []
     #def isEmpty(self):
     #    return self.arr == []
     
#     def enqueue():
 
#     def dequeueAny():
    
#     def dequeueDog():

#     def dequeueCat():
        

# -----------------------------------
# StackQueue 06: Stack of Plates:
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific substack.
# Q:
# Sol:

# -----------------------------------
# StackQueue 07: Three in One, implement three stacks in a single array.
# Given:    Hints: #2, #72, #38, #58
n = 10

# Sol1: Assign n/3 size to each stack
arr1 = n//3*[]

# Sol2: Grow paritition size when one stack exceeds capacity
     # also design the array circularly --> solution too long, do later


# -----------------------------------
# StackQueue 08: Reverse a stack without using extra space in O(n)
# Sol:
def s_reverse(s): 
    ll = LinkedList()                           # start an empty LL object            
    node1 = Node(1);    LL.head = node1    
    node2 = Node(2);    node1.next = node2
    
    
    