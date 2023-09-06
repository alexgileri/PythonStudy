# Contents: Heap Construction/Ops, Trie Construction/Ops, Q

for var in dir():
    if not var.startswith('_'):
        del globals()[var]


# -----------------------------------
# Heaps: Build a max heap wheer parents are always larger, so need to fix bottom up fashion
# - Used for..
def heapify(arr, n, i):  # n is size of heap
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:  # See if left child exists and is greater than root
        largest = l
    if r < n and arr[largest] < arr[r]:  # vv
        largest = r

    if largest != i:  # change root, if needed
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # heapify the root.

def heapify(arr, n, i):     # O(n)
    p = i                   # heapify subtree of size n rooted at index i
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

arr = [4, 10, 3, 5, 1]
heapSort(arr)


# -----------------------------------
# Tries:
# - Used for..
class Trie:
    def __init__(self):
        self.children = {}  # mapping from character ==> Node
        self.value = None

def find(node, key):
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value


class TrieNode: 
    def __init__(self): 
        self.children = [None]*26   # alphabet      
        self.isEndOfWord = False    # True if node represent the end of the word 
  
class Trie:      
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self):               
        return TrieNode()   # initialized to None
  
    def _charToIndex(self, ch):     # assume lower case           
        return ord(ch)-ord('a')     # converts key current character into index 
  
    def insert(self,key):         
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]:   # if char is not present
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index]          
        pCrawl.isEndOfWord = True   # mark last node as leaf after inserting
  
    def search(self, key):                           
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
        return pCrawl != None and pCrawl.isEndOfWord 
  
keys = ["the","a","there","anaswe","any", "by","their"] 
output = ["Not present", "Present"]   
t = Trie()  
for key in keys:    # construct
    t.insert(key)   
# Search for different keys 
#print("{} ---- {}".format("the",output[t.search("the")])) 
output[t.search("the")]         # yes
output[t.search("these")]       # nope
output[t.search("their")]       # yes
output[t.search("thaw")]        # nope

