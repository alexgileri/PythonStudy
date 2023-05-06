# Contents: BT Construction/Ops, Q

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var
import math


# -----------------------------------
# BinaryTree: Access (search/sort/insert) = O(logn), Space = O(m*10^n)
# - Usage: quick access (better than Htables), range querry, finding closest smaller/larger
# - full-balanced: 2^n-1 elements, n levels
# - preorder: traverse parent to child
class BinaryTree:
    def __init__(self, root):
        self.root = root        

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def bst_insert(self, data):     # BST style insert
        if self.data:
            if data < self.data:    # compare the new value with the parent node
                if self.left is None: # no node yet
                    self.left = Node(data)
                else:  
                    self.left.insert(data)  # there's a node but wanna overwrite
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data        
    
    def set_left(self, data):       # direct insert
        if self.left is None:   # no node yet
            self.left = Node(data)
    def set_right(self, data):       # direct insert
        if self.right is None:   # no node yet
            self.right = Node(data)            
                
    def print_node(self):   # inorder
        if self.left:
            self.left.print_node()  # recursive print left nodes first
        print(self.data)    # print root
        if self.right:      # print right nodes
            self.right.print_node()

    def inorder(self, root):    # Left -> Root --> Right 
        res = []
        if root:                # 
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res
    
    def postorder(self, root):    # Root --> Left --> Right 
        res = []
        if root:
            res = self.postorder(root.left)              
            res = res + self.postorder(root.right)       
            res.append(root.data)                # 
        return res
    
    def preorder(self, root):    # Left --> Right --> Root
        res = []
        if root:      
            res.append(root.data)     # 
            res = res + self.preorder(root.left)              
            res = res + self.preorder(root.right)       
        return res
    
    def bfs(self, root):    # Lparent --> Lchildren --> Rparent --> Rchildren
        res = []
        q = [root]   # queue of visited nodes
        while len(q)>0:   # while + pop = go back and retry until all queue popped
            node = q.pop(0)      # 1st layer 
            res.append(node.data)
            if node.left: 
                q.append(node.left)
            if node.right:  
                q.append(node.right)                   
        return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

root.inorder(root)
        
root = Node(1)  
root.left = Node(2)  
root.right = Node(3) 
root.left.left = Node(4)  
root.left.right = Node(5)  
root.left.right.left = Node(6)  

root.inorder(root)      # 4 2 5 1 3  # Left --> Root --> Right --> for searching BST
root.preorder(root)     # 4 5 2 3 1  # Root --> Left --> Right --> for copying BT
root.postorder(root)    # 1 2 4 5 3  # Left --> Right --> Root --> for deleting BT

root.bfs(root)          # 1 2 3 4 5  # Root --> Left --> Right but level order (iterative)


# -----------------------------------
# QUESTIONS
# -----------------------------------
# BinaryTrees 01: Insert the key into a BT at first position available in
# Q: what do you mean by first? --> level order (vertical)

# Sol: BFS style search
def insert_bt(root, key):   #
    q = []              # queue
    q.append(root)   
    # Do level order 
    while len(q):
        temp = q[0]  
        q.pop(0)    # pops the left one first
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
      
        if not temp.right:
            temp.right = Node(key)
            break
        else: 
            q.append(temp.right)  
    return None
insert_bt(root, 7)   
root.bfs(root)      # ..5, 7, 6 becuase of level order insert


# -----------------------------------
# BinaryTrees 02: Put a BT in an array
# Given: same tree --> # arr = [1, 2, 3, 4, 5, 7, None, None, None, 6, None]
# Sol: fill with BFS
arr = 15*[None]
q = [root]                  # queue of visited nodes
arr[0] = root.data
i = 0
while len(q)>0:             # while + pop = go back and retry until all queue popped
    node = q.pop(0)         # 1st layer 
    #arr.append(node.data)
    if node.left: 
        q.append(node.left)
        arr[2*i+1] = node.left.data
    
    if node.right:  
        q.append(node.right) 
        arr[2*i+2] = node.right.data
    i = i + 1    
arr
# root.bfs(root)    # to double check

# Sol 2: Recur --> FIX
def bt2array2(node, arr, i):
    #i = 0
    if not node:
        return arr    
    else:
        print(i, arr)
        if node.left: 
            arr[2*i+1] = node.left.data 
            node = node.left
        if node.right:     
            arr[2*i+2] = node.right.data
            node = node.right
        else:
            return arr
        bt2array2(node.left, arr, i+1)
        bt2array2(node.right, arr, i+1)    
    #return arr   
arr = 12*[0]
bt2array2(root, arr, 0)

    
# -----------------------------------
# BinaryTrees 03: Form a BT from an array  --> FIX
# Given: same tree 
# Sol: fill with BFS
arr = [1, 2, 3, 4, 5, 7, None, None, None, 6, None]
n = len(arr)

def array2bt(arr, i): 
    if n==0:
        return None
    elif n==1:
        return arr[1]
    else:         
        node = Node(arr[1])
        while i < n:
            node = arr[i]   # parent
            if 2*i+1 < n:
                if arr[2 * i + 1] != None:    # set left child
                    node.set_left(arr[2*i+1])
            if 2*i+2 < n:
                if arr[2 * i + 2] != None:    # set right child
                    node.set_right(arr[2*i+2])
                
                print("node", arr[i], "setting children:", arr[2*i+1], arr[2*i+2])
            array2bt(arr, i+1)  # recur
        return node    
array2bt(arr, 0)
# root.bfs(root)  # check
    
    
# -----------------------------------
# BinaryTrees 04: Find the height of a BT
# Given: previous tree --> 4

# Sol 1: Recur
def height1(node): 
    if node is None: 
        return 0 
    else: 
        lheight = height1(node.left)     # reach left bottom first (inorder)
        rheight = height1(node.right)    #         
        if lheight > rheight:           # 
            return lheight + 1          # base case is None (cnt = 0)
        else:                           # from a same branch, each children bring a count
            return rheight + 1          # parent takes the highest one, meaning that kid
                                        # has more family generations        
height1(root)

# Sol 2: Iter, 
def height2(node): 
    if node is None: 
        return 0 
    else: 
       h = 1
       if node.left or node.right:
           h = h + 1
           

# -----------------------------------
# BinaryTrees 05: Find the # of leaves in a BT
# Given: previous tree --> 3
           
# Sol:
def count_leaves(node): 
    if node is None: 
        return 0 
    else: 
        lheight = height1(node.left)     # reach left bottom first (inorder)
        rheight = height1(node.right)    #         
        if lheight > rheight:           # 
            return lheight + 1          # base case is None (cnt = 0)
        else:                           # from a same branch, each children bring a count
            return rheight + 1         
count_leaves(root)


# -----------------------------------
# BinaryTrees 06: HeapSort, build a Max heap (heapify)
    # Max heap: parents are always larger --> need to fix bottom up fashion
arr = [4, 10, 3, 5, 1]

# Sol: O(logn)
def heapify(arr, n, i): # O(n)
    p = i               # heapify subtree of size n rooted at index i
    l = 2*i + 1 
    r = 2*i + 2     
    if l < n and arr[i] < arr[l]: # if left child exists and it is greater
        p = l 
    if r < n and arr[p] < arr[r]: # same for right child
        p = r 
  
    if p != i:                      # if a greater children found earlier
        arr[i], arr[p] = arr[p], arr[i] # swap the root with that one         
        heapify(arr, n, p)           # Heapify the root
    
def heapSort(arr):      # O(nlogn)
    n = len(arr) 
    for i in range(n, -1, -1):   # build a maxheap
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1):         # One by one extract elements 
        arr[i], arr[0] = arr[0], arr[i]     # swap 
        heapify(arr, i, 0)   
    return arr
heapSort(arr)


# -----------------------------------
# BinaryTrees 07: Left view of a BT
# Q: order matters? --> top down
# Given: previous tree --> 1->2->4       

# Sol: BFS + print the first node in every level
def left_view(node):      # start with root
    if node == None:
        return  # terminate    
    res = [node.data]
    q = [node]   # queue of visited nodes
    while len(q) > 0:   # while + pop = go back and retry until all queue popped
        node = q.pop(0)      # 1st layer 
        if node.left: 
            res.append(node.left.data)
            q.append(node.left)
        if node.right:  
            q.append(node.right)                   
    return res         
left_view(root)        


# -----------------------------------
# BinaryTrees 07: Top view of a BT
# Q: order matters? --> left to right
# Given: previous tree --> 4->2->1->3       

# Sol: BFS + print the first node in every level
def top_view(node):   # terminate if root = None   
    res = [node.data]
    q = [node]
    while len(q) > 0:
        node = q.pop(0)
        if node.left: 
            res.append(node.left.data)
            q.append(node.left)
        if node.right:  
            q.append(node.right)                   
    return res         
top_view(root)        


# -----------------------------------
# BT: Bottom view of a BT
# Q: order? --> left to right again
# Given: previous tree --> 4->6->5->7->3       

# Sol: in order
def top_view(node):   # terminate if root = None   
    res = [node.data]
    q = [node]   # queue of visited nodes
    while len(q) > 0:   # while + pop = go back and retry until all queue popped
        node = q.pop(0)      # 1st layer 
        if node.left: 
            res.append(node.left.data)
            q.append(node.left)
        if node.right:  
            q.append(node.right)                   
    return res         
top_view(root) 


# -----------------------------------
# BT: Clone a BT
def clone_bt(node):   # terminate if root = None   
    res = [node.data]
    q = [node]
    while len(q) > 0:
        node = q.pop(0)
        if node.left: 
            res.append(node.left.data)
            q.append(node.left)
        if node.right:  
            q.append(node.right)                   
    return res
        
clone_bt(root) 

# -----------------------------------
# BinaryTrees 10: Miror a BT

