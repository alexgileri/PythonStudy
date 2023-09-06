# Contents: LinearSearch, BinarySearch, JumpSearch, InterpolationSearch,
          # BubbleSort, QuickSort, MergeSort, InsertionSort, SelectionSort, Q

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
import math


# -----------------------------------
# SEARCH SEARCH

# 1) LinearSearch (O(n), O(1))              # best if unsorted
def linear_search(arr, val):
    n = len(arr)
    cnt = 0
    for i in range(n):
        #print(i)
        if arr[i] == val :
            #break
            cnt = cnt + 1
            return i                        # return the index of the finding
    return -1


# 2) BinarySearch (O(logN), O(1))           # best if monotonic
def binary_search(arr, val):
    n = len(arr)
    i = int(round(n / 2, 0))
    cnt = 1
    while i < n:
        # print(i)
        if arr[i] == val:
            return i;
        # break
        elif arr[i] > val:
            cnt = cnt + 1
            i = i - int(round((n / (2**cnt)), 0))

        else : # arr[i] < val:
            cnt = cnt + 1
            #i = i - math.ceil(n/(2**(cnt)))\
            i = i + int(round((n / (2**cnt)), 0))
    return -1

def binary_search2(arr, val):                # faster for large i/p, just +1 iter
    n = len(arr)
    l = 0
    r = n-1                                 # left/right pointers of the region of interest
    cnt = 1                                 # iter counter
    #global i
    while l < r :                           #
        i = math.floor((r+l)/ 2)            # returns int anyway
        #print(cnt, i, l, r)
        if arr[i] < val:                    # search right, or carry the left pointer to mid
            cnt = cnt + 1
            l = i + 1                       # +1 because first index 0 convention
        else : # arr[i] > val
            cnt = cnt + 1
            r = i
        return -1
    return l                                # checks only when L = R, where the speed comes from


# 3) JumpSearch (O(sqrtN), O(1)), AKA block search, slower but jumps back lesser (n/m jumps)
def jump_search(arr, val):
    n = len(arr)
    m = math.sqrt(n)                        # jump step location set
    i = 0
    r = n-1
    cnt = 0
    while arr[i] < val:
        cnt = cnt + 1
        #print(cnt, i)
        i = i + round(m)                    # move left pointer to next chunk
        if i >= n:                          # if overflows, then target out of range
            return -1
        #else                               # i jumped over val, scan back previous chunk
    while arr[i] > val:                     # scan backwards from current i
        cnt = cnt + 1
        #print(cnt, i)
        i = i - 1;
    return i


# 4) InterpolationSearch (O(loglogN)))      # shines if the elements are uniformly distributed
def interp_search(arr, val):
    n = len(arr)
    l = 0
    r = n-1
    cnt = 0
    i = 0
    while (arr[i] < val) and (arr[l] < val < arr[r]):
        i = l + int( (val - arr[l]) * (r - l) / (arr[r] - arr[l]) )  # like my boost search
        cnt = cnt + 1
        # print(cnt, i)
        if arr[i] == val:                   # if found, return
            return i
        elif arr[i] < val:
            l = l + 1
        else : # arr[ i ] < val:
            r = r -1
    return -1                               # if the scan is complete and it's not found

# 5) ExponentialSearch (?)
# 6) TernarySearch (?)
# 7) SublistSearch (?)
# 8) FibonacciSearch (?)
# ex) Ubiquitious BinarySearch (?)
# ex) Recursive LinearSearch (?)
# ex) Recursive Substring Search (?)
# ex) Unbounded BinarySearch (?)

    
# -- Test
arr = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]       # sorted
n = len(arr)
val = 8;

linear_search(arr, val)
binary_search(arr, val)
binary_search2(arr, val)         # failed for repeating numbers in arr
jump_search(arr, val)
interp_search(arr, val)


# -----------------------------------
# SORT SORT

# 1) BubbleSort: O(n^2)/O(1), best for fixing few items in a big array, worst for reverse sorted
def bubble_sort(arr):
    for i in range(len(arr)) :
        swapped = False                     # for optimization
        for j in range(0, len(arr)-i-1) :   # i is used only here to define the range
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False :               # if carrying a j didn't cause any swaps along the way,
            break                           # the rest of the array is sorted already, break
    #for j in range(n) :
        #print (arr[j], end=' ')            #
        #print ("%d" %arr[j], end=' ')      # alternatively


# 2) QuickSort: O(n^2)/O(n+k), D&C algo, good for Arrays since need random access as x + i*4
def part(arr, L, R):
    i = L - 1                               # index to place the vals found, start at -1
    #j = L                                  # index to compare to pivot
    for j in range(L, R):                   # pivot is the R
        #print(L, R, i, j, arr)
        if arr[j] < arr[R]:                 # if smaller value found     # removed <=
            i = i + 1                       # prepare it's index (i)
            arr[j], arr[i] = arr[i], arr[j] # switch it with (j)
            #arr[j] = arr[i]                # places smaller elements to left of pivot and vv.
            #arr[i] = temp                  #
    temp = arr[R]                           # since 0-i contains smaller than pivot,
    arr[R] = arr[i+1]                       # place pivot at i+1
    arr[i+1] = temp
    #print(L, R, i, j, arr)                  # double check the pivot placement
    return i+1                              # pivot is placed at i, it's sorted!

def quick_sort(arr, L, R):                  # recursion to divide, real issue is to merge
    if L < R:
        pivot = part(arr, L, R)
        quick_sort(arr, L, pivot-1)         # sort left
        quick_sort(arr, pivot + 1, R)       # sort right


# 3) MergeSort: O(nlogn)/O(?), D&C algo, good for LLs since mid-insert O(1)
def merge_sort(arr):                        # recursion to divide, real issue is to merge
    if len(arr)>1:                          # no need of n since calculates length recursively
        mid = len(arr)//2                   # quotient --> last ones: 3/2 = 1 --> [n0], [n1 n2]
        lefthalf = arr[:mid]                # exclusive (n0)
        righthalf = arr[mid:]               # inclusive (n1, n2)
        merge_sort(lefthalf)                # recursion
        merge_sort(righthalf)               # sort till the bottom branch complete
        i, j, k = 0, 0, 0                   # indexes of arrL/arrR/arr_merged
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:  # if n0 < n1
                arr[k] = lefthalf[i]        # place n0 to k = 0
                #print("Merging i=", i, arr)
                i = i+1
            else:
                arr[k] = righthalf[j]       # o.w. pick n1 for k = 0
                #print("Merging j=", j, k, arr)
                j = j+1
            k=k+1                           # always inc

        while i < len(lefthalf):            # if left lenght is smaller, won't exec
            arr[k] = lefthalf[i]            #
            #print("Bypassing i=", i, arr)
            i = i+1
            k = k+1                         # left bypass completed
        while j < len(righthalf):           # j = 1, n2 remaining, bypasses
            arr[k] = righthalf[j]           # copied over n2, since n2>n1 in prev step
            #print("Bypassing j=", j, arr)
            j = j+1
            k = k+1                         # right bypass completed


# 4) InsertionSort: O(n^2)/O(1), maintains a sorted sublist in the low part, good for kinda sorted
def insert_sort(arr):
    for i in range(1, len(arr)):            #
        for j in range(0, i):               # scan a sublist
            if arr[i] < arr[j]:             # if found a smaller element
                temp = arr[i]               # save it
                arr[i] = arr[j]             # insert it
                arr[j] = temp               # finish the swap
                #break
            print(i, j, arr)
            #else : # arr[j] >= arr[j+1] :   # o.w. carry on to find a bigger right neighbor

def insert_sort2(arr):                      # instead of swapping i/j, just insert i
    for i in range(1, len(arr)):            # this will cause a shift though
        for j in range(0, i):               # scan a sublist
            if arr[i] < arr[j]:             # if found a smaller element
                arr.insert(j, arr.pop(i))   # insert ith to jth location
                #break
            #print(i, j, arr)
            #else : # arr[j] >= arr[j+1] :   # o.w. carry on to find a bigger right neighbor
    return arr


# 5) SelectionSort: O(n^2)/O(1), 1 exchange per pass, n−1  passes, good for reverse sorted
def select_sort(arr):                       #
    for i in range(0, len(arr)):            #
        jmax = 0  # temp max index = assume 1st element is max
        for j in range(1, len(arr)-i):      # scan till the last sorted sublist
            #print(i, j, jmax, arr)
            if arr[j] > arr[jmax]:          # if found a smaller element
                jmax = j  # update max      # //        index

        temp = arr[len(arr)-i-1]            # save the last element (before the subarray)
        arr[len(arr)-i-1] = arr[jmax]       # place vmax on it
        arr[jmax] = temp                    # swap the last element with the max element found


# 6) HeapSort O(nlogn)/O(1), fixed speed regardless of i.c., can be iterative

# 7) Counting Sort: O(?)/O(n+k), no comparison, goof if input is bounded by [1 k], sort by digits,

# 8) RadixSort: O(logb(k)*(n+b))/O(?), no comparison, good if input is bounded by [1 k^2]
# -Better than QuickSort if log2n bits/digits (binary)
# - b = base (10 for decimals), k = sqrt(bound), n = input size

# 9) Bucket Sort: O(?)/O(?)


# -- Test
arr = [9, 9, 7, 8, 8, 5, 4, 0, 1, 2, 7, 7]
arr_org = arr
bubble_sort(arr);   print(arr)
quick_sort(arr, 0, len(arr)-1); print(arr)
merge_sort(arr);    print(arr)
insert_sort2(arr);  print(arr)
select_sort(arr);   print(arr)
# heap_sort(arr);   print(arr)
# count_sort(arr);  print(arr)
# radix_sort(arr);  print(arr)
# bucket_sort(arr);  print(arr)


# -----------------------------------
# QUESTIONS
# -----------------------------------
# SearchSort 01: Sort a list according to the second element in sublist
arr = [['c', 2], ['b', 1], ['a', 3]  ]   # out = [['b', 1], ['c', 2], ['a', 3]
n = len(arr)

# Sol: Bubble
# bubble_sort(arr)        # sorts wrt 1st element, not 2nd
for i in range(n):
    for j in range(1, n-i):
        if arr[j-1][1]> arr[j][1] : 
            arr[j-1], arr[j] = arr[j], arr[j-1]
arr


















