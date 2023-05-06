# Contents: LL Construction/Ops, Q

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var
import math


# -----------------------------------
# LinkedLists: Chain of nodes containing data and (next) link. First data is Head, last link is Null
# - O(n) index/search same as arrays, O(1) insert/delete better than arrays. Dynamic, unlimited size
# - Cons: No random access and extra space for the link, bad locality in cache (distributed)

class Node:         # better to put it in LinkedList() if multiple things point to the head
    def __init__(self, data):           # init an node
        self.data = data                # assign data if given, o.w. null
        self.next = None                # init a null next
        
    def print_node(self):
        temp = self.data
        if temp:                        # if there's a data there?
            print(self.data)        

class LinkedList:
    def __init__(self):                 # init the head
        self.head = None                # why not data?
    
    def len_ll(self):
      temp = self.head
      cnt = 0
      while temp:  # if there's a data there?
          cnt = cnt + 1
          temp = temp.next  # go to next data
      return cnt 
    
    def print_ll(self):
        temp = self.head
        while temp:                     # if there's a data there
            print(temp.data, end =" ")
            temp = temp.next       # go to next node index
        print("\r")    

    def get_data(self, n):
        temp = self.head
        cnt = 0                         # node counter
        while temp and (cnt<n):         # instead of cnt < n, can do 
        #while temp and (temp.data == val): # alternative if value input
            #if cnt == n:
            temp = temp.next             # go to next node index
            cnt = cnt + 1
        return temp.data

    def set_data(self, n, val):
        temp = self.head                # start scanning from head till..
        cnt = 0                         # node counter
        while temp and (cnt<n):         # there's a data            
            temp = temp.next            # go to next node index
            cnt = cnt + 1               # eventually reaches n
        temp.data = val                 # then value is inserted there
        
    def ins_data(self, n, val):             #       
        temp = self.head
        cnt = 0
        if n == 0:                          # if inserting to the head
            self.head = Node(val)
            self.head.next = temp           # previous head becomes the next
        else:        
            while temp and (cnt < n-1):     # append --> just remove cnt < condition    
                # if cnt == n:
                temp = temp.next            
                cnt = cnt + 1                    
            new_node = Node(val)            # create the node to be inserted
            new_node.next = temp.next       # make next of new Node as next of prev_node  
            temp.next = new_node            # link the given node to this node           
        
    def del_data(self, n):                  # deletes n-th node
        temp = self.head
        cnt = 0  # node counter
        if n == 0:
            self.head = temp.next
            temp = None
        else:
          while temp and (cnt < n-1):            
              # if cnt == n:
              temp = temp.next            
              cnt = cnt + 1
          bad_node = temp.next
          temp.next = temp.next.next
          #del bad_node                     # free from memory
          bad_node.next = None              # alternative

LL = LinkedList()                           # start an empty LL object            
node1 = Node(1);    LL.head = node1    
node2 = Node(2);    node1.next = node2
node3 = Node(4);    node2.next = node3
node4 = Node(6);    node3.next = node4
node5 = Node(8);    node4.next = node5
node5.next = None


# -----------------------------------
# LinkedList 01: Print LL and Get length
# Sol1: 
def len_ll(ll):  # get the length
    temp = ll.head
    cnt = 0
    while temp:
        cnt = cnt + 1
        temp = temp.next
    return cnt  #
len_ll(LL)                                  # get length
LL.head.print_node()                        # print the head

# Sol2: Recursive, return (1+count(head --> next))
def len2_ll(node):          # provide the node this time
    #temp = ll.head
    # cnt = 0
    if not node:
        #cnt = cnt + 1
        #temp = temp.next
        return 0        #   
    else:                # +1 at each recursion
        return 1 + len2_ll(node.next)  # 1 here counts, stops when None
        node.print_node()
len2_ll(LL.head)                            # test the recursion


# -----------------------------------
# LinkedList 02: Get / Set data at n-th position
# Sol1: 
LL.get_data(0)                              # get first node
LL.get_data(len_ll(LL)-1)                   # get last node

LL.set_data(0, 'a')                         # set first node
LL.head.print_node()
LL.set_data(len_ll(LL)-1, 'b')              # set last node     
LL.print_ll()


# -----------------------------------
# LinkedList 03: Insert / Delete data at n-th position
# Sol1: 
LL.ins_data(0, 'aa')                        # insert to first node               
LL.ins_data(len_ll(LL), 'bb')               # insert to last node (not len-1)
LL.print_ll()

LL.del_data(0)                              # delete first node
LL.del_data(len_ll(LL)-1)                   # delete last node
LL.print_ll()


# -----------------------------------
# LinkedList 04: Delete a LL
# Sol1: 
def delete_ll(ll):
    temp = ll.head                          # current node
    #cnt = 0
    while temp:                           # if there's a data there?
       # cnt = cnt + 1
        nextt = temp.next                   # go to next data
        #curr.data = None                   # still consumes 16bytes
        del temp.data
        temp = nextt
    return None

LL.print_ll()
delete_ll(LL)
LL.print_ll()                               # error since no data


# -----------------------------------
# LinkedList 05: Find mid node of a LL
# Sol: O(1.5n) = O(n)
def find_mid(ll):
    temp = ll.head
    cnt = 0
    while temp:
        temp = temp.next
        cnt = cnt + 1  
    temp = ll.head         
    for i in range (0, math.floor((cnt-1)/2)):
        print(i, temp.data)
        temp = temp.next
    return temp.data

LL.print_ll()
find_mid(LL)
LL.ins_data(len_ll(LL), 'a')
find_mid(LL)
LL.ins_data(len_ll(LL), 'b')
find_mid(LL)


# -----------------------------------
# LinkedList 06: Delete the mid node of a LL
# Sol 1: Use previous method
# Sol 2: Use fast/slow pointers
def del_mid(ll):     
    ptr_fast = ll.head
    ptr_slow = ll.head    
   # cnt = 0
    while ptr_fast and ptr_fast.next:         # no need to check for the slow
        ptr_fast = ptr_fast.next.next
        prev = ptr_slow
        ptr_slow = ptr_slow.next  # next ptr, already passed the mid
    prev.next = ptr_slow.next    # connext previous to next ptr
    del ptr_slow
        #print(i, temp.data)
        #temp = temp.next
    return 0
LL.print_ll()
del_mid(LL)
LL.print_ll()
LL.ins_data(len_ll(LL), 'a')
LL.print_ll()
del_mid(LL)         # deletes (n+1)/2 instead of (n-1)/2 but who cares
LL.print_ll()


# -----------------------------------
# LinkedList 07: Find the n-th node in a LL
# Given:
n = 1
# Sol:
def find_nth(ll, n):
    node = ll.head
    cnt = 1             # 0 is not a counting number
    while node:        
        if cnt == n:
            return node.print_node()
        else: 
            node = node.next
            cnt = cnt + 1   
LL.print_ll()           
find_nth(LL, 3)     # = 6

# Mod: Find the n-th node from the end
# Sol: 2 ptr with n delta, wait for the ptr2 to reach end
def find2_nth(ll, n):
    ptr1 = ll.head
    ptr2 = ll.head      # ahead with n
    cnt = 1             # 0 is not a counting number
    while ptr2: 
        if cnt == n:
            ptr2.print_node()
            return None 
        else:
            cnt = cnt + 1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
    return ptr1.data

LL.print_ll()
find2_nth(LL, 3)    # = 6


# -----------------------------------
# LinkedList 08: Search an element in a LL
# Sol 1: Iterative, O(n)/O(1)
def search_data(ll, val):
    temp = ll.head
    while temp:
        if temp.data == val:
            return True
        temp = temp.next
    return False
LL.print_ll()
search_data(LL, 6)      # True

# Sol 2: Recursive
def search2_data(node, val):    
    #if node.data == None:
    if node == None:
        print("the end")
        return False
    else: 
        if node.data == val:
            print("match at node:", end = " ")
            node.print_node()   
            return True
        return search2_data(node.next, val)
LL.print_ll()
search2_data(LL.head, 6)      # True


# -----------------------------------
# LinkedList 09: Count an element in a LL
# Sol1: Iterative, O(n)/O(1)
def count_data(ll, val):
    temp = ll.head
    cnt = 0
    while temp:
        if temp.data == val:
            cnt = cnt + 1
        temp = temp.next
    return cnt
LL.print_ll()          
count_data(LL, 2)
LL.ins_data(len_ll(LL), 2)
cnt = count_data(LL, 2)

# Sol2: Recursive, need to keep handing a counter, unless defined as self (class)
def count2_data(node, val, cnt):
    print("cnt =", cnt, end = ": ")
    if node == None:        # count till end, node vs None, not node.data
        print("the end")
        return cnt
    else:
        if node.data == val:      # won't excecute after return anyway
            print("match at node:", end = " ")
            node.print_node()
            cnt = cnt + 1            
        else:         
            print("no match")
        return count2_data(node.next, val, cnt)    # regarless of match, keep recursing    
#LL.ins_data(4, 2)    # insert few more 2s to test
#LL.ins_data(4, 2)  
LL.print_ll()
count2_data(LL.head, 2, 0)
# LL.head.next.data == 2


# -----------------------------------
# LinkedList 10: Remove duplicates from a sorted LL
# Given:
LL = LinkedList()                           # start an empty LL object            
node1 = Node(1);    LL.head = node1    
node2 = Node(2);    node1.next = node2
node3 = Node(2);    node2.next = node3
node4 = Node(2);    node3.next = node4
node5 = Node(3);    node4.next = node5
node6 = Node(3);    node5.next = node6;     
node6.next = None       # out = 1 2 3

# Sol:
LL.print_ll()
n = len_ll(LL)  # ll length
node = LL.head  # init node
i = 1           # ll index
while node.next and (1 <= i <= n) :
    print(i, n, node.data) 
    if node.next.data == node.data : # if next data is same, delete next data
        LL.del_data(i)  
        n -= 1          # length decrease s after deletion   
        print("duplicate found\n")
    else:
        node = node.next  
        i += 1          # go to next node
LL.print_ll()        

# Mod: .. unsorted LL
LL = LinkedList()                           # start an empty LL object            
node1 = Node(9);    LL.head = node1    
node2 = Node(8);    node1.next = node2
node3 = Node(7);    node2.next = node3
node4 = Node(7);    node3.next = node4
node5 = Node(8);    node4.next = node5    
node5.next = None       # out = 1 2 3

# Sol: hashing
hashd = dict()      # hashtable dictionary
LL.print_ll()
n = len_ll(LL)      # ll length
i = 1               # ll index
node = LL.head  # init node

while node.next and (1 <= i <= n) :
    print(i, n, node.data) 
    # if node.next.data not in hashd.keys():   
    if hashd[node.next.data] == 0:          # if unique 
        node = node.next                    
        i += 1                              # go to next node
    else:
        hashd[node.next.data] = 1           # record it
        LL.del_data(i)  
        n -= 1          # length decrease s after deletion   
        print("duplicate found\n")


# -----------------------------------
# LinkedList 11: Find intersection point of 2 LLs
# Q: same data? --> no same reference to the node
    # sorted? --> not relevant
LL1 = LinkedList()
node1 = Node(1);    LL1.head = node1    
node2 = Node(2);    node1.next = node2
node3 = Node(3);    node2.next = node3
node4 = Node(4);    node3.next = node4
node4.next = None
LL2 = LinkedList()
node5 = Node(9);    LL2.head = node5
node5.next = node3   # here is the intersection
LL1.print_ll()
LL2.print_ll()     

# Sol 1: Hashing, go back from last node
# Sol 2: Traverse the longer LL till lengths are same and then check,(O(m+n)/O(1)
def inter_point(ll1, ll2):
    n1 = len_ll(ll1)
    n2 = len_ll(ll2) 
    if (n1 == 0) or (n2 <= 0):
        return False        # can't find
    ll1node = ll1.head
    ll2node = ll2.head
    if (n1 == n2) and (ll1node == ll2node) :
        return ll1node.data    # if intersect at the first node
    else : 
        if n1 > n2 :            
            for i in range(n1-n2) :
                ll1node = ll1node.next      # iterate till same lengths
        else : # n1 < n2 :            
            for i in range(n2-n1) :
                ll2node = ll2node.next      # //      
        if ll1node.next == ll2node.next :  # check if same address
            return ll1node.next.data         
    return False        
inter_point(LL1, LL2)


# -----------------------------------
# LinkedList 12: Find intersection (not the point) of 2 sorted LLs
# Q: duplicate elements --> yes, element is an element
LL3 = LinkedList();   LL3.head = Node(2)    # intersect(LL1, LL3) 
LL3.head.next = Node(4);
LL3.head.next.next = Node(5);
LL3.head.next.next.next = None   # inter = [2 4]
LL1.print_ll()
LL3.print_ll()  

# Sol: 2ptr method, O(m+n)/O(1)
def intersect(ll1, ll2):
    n1 = len_ll(ll1)
    n2 = len_ll(ll2)
    res = []
    if (n1 == 0) or (n2 == 0) :
         return False   # can't find
    else : 
        ll1node = ll1.head
        ll2node = ll2.head
        if ll1node.data == ll1node.data :
            res.append(ll1node.data)
            
        while ll1node and ll2node :  # if both lists are not traversed yed
            if ll1node.data == ll2node.data :
                res.append(ll1node.data)
            elif  ll1node.data > ll2node.data :
                ll1node = ll1.head
                ll1node = ll1node.next      # iterate till same lengths
        else : # n1 < n2 :            
            for i in range(n2-n1) :
                ll2node = ll2node.next      # //      
        if ll1node.next == ll2node.next :  # check if same address
            return ll1node.next.data         
    return False        
inter_point(LL1, LL2)

# Mod: Union of .. 
# Sol:


# -----------------------------------
# LinkedList 13: Merge A Linked List Into Another Linked List At Alternate Positions


# -----------------------------------
# LinkedList 14: Reverse a LL efficiently
# Q: access to length? --> yes      
# Sol 1: Stack, O(n) but uses temp var
def reverse_ll1(ll) :
    stack = []
    n = ll.len_ll() 
    node = ll.head
    res = []
    for i in range(n):
        stack.append(node.data)
        node = node.next
    for i in range(n):
        res.append(stack.pop())
    return res
reverse_ll1(LL1)

# Sol 2: Exhaustive, O(n^2)
def reverse_ll2(ll) :    
    n = ll.len_ll()
    res = []
    for i in range(n-1, -1, -1):
        res.append(ll.get_data(i))
    return res
reverse_ll2(LL1)

# Sol 3: Cheat using print \r
def reverse_ll3(ll) :
    n = len_ll(ll) 
    node = ll.head
    for i in range(n):
        # if node != None:        # node vs None, not node.data
        print((n-i-1)*2*" ", node.data, end="\r")
        node = node.next        
    return None
reverse_ll3(LL1)


# -----------------------------------
# LinkedList 15: Wanna add 1 to LL of digits.  
# Q: What is the time complexity? --> O(?)

# Given: 
arr = [1, 2, 4, 6, 8]  # 12,468 + 1 = 1->2->4->6->9 (LL)
n = len(arr)

# Sol1: 
    #head = Node(arr[0])
    #for i in range(n-1):
    #    print(i)
    #    head
    #    Node(arr[i]).next = Node(arr[i+1])
    #LL.head = Node(arr[0])
    #len_ll(LL)
    #LL.print_ll()   
def add1(ll):         # add 1 method
    carry = 1
    lenLL = len_ll(ll)
    #ll_arr = [0]*lenLL
    for i in range(0, lenLL):
        # i = 0
        digit = ll.get_data(lenLL-1 - i)
        if (digit == 9)and (carry ==1) :  # if last digit = 9
            ll.set_data(lenLL-1 - i, 0)  # it'll overflow and become 0
            #carry = 1
        else:
            ll.set_data(lenLL - i - 1, digit + carry)
            carry = 0
     #   ll_arr[len_ll-1 - i] = ll.getn(len_ll-1 - i)
    #return ll_arr
LL.print_ll()
add1(LL)
LL.print_ll()
add1(LL)                            # test for the carry
LL.print_ll()


# -----------------------------------
# LinkedList 16: Add 2 numbers stored in LLs in forward order 

# Mod: reverse order


# -----------------------------------
# LinkedList 17: Select A Random Node from a LL


# -----------------------------------
# LinkedList 18: Swap nodes in a LL without swapping data

# -----------------------------------
# LinkedList 19: Pairwise swap elements of a given LL

# -----------------------------------
# LinkedList 20: Segregate even and odd nodes in a Linked List

# -----------------------------------
# LinkedList 21: Partition a LL around x s.t. all nodes <x come before all nodes >=x

# -----------------------------------
# LinkedList 22: Function to check if a singly linked list is palindrome

# -----------------------------------
# LinkedList 23: Detect, find the length and remove a loop in a LL and 

# -----------------------------------
# LinkedList 24:Reverse A List In Groups Of Given Size

# -----------------------------------
# LinkedList 25:Compare two strings represented as linked lists

# -----------------------------------
# LinkedList 26:Move last element to front of a given Linked List

##-----------------------------------
# LinkedList 27: QuickSort on LLs

# -----------------------------------
# LinkedList 28: Mergesort on LLs

