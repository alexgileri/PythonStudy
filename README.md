## Description
Python study notes with practice questions


## Content

| Script                     | Contents                                                                                                       |  
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| 00_CleanCode               | Zen, Indentation, Commentation, Quotation, Spacing (Char/Line), Namespaces, Encoding                           |
| 01_DataTypes               | Numbers, Strings, Lists, Tuples, Dictionary                                                                    |
| 02_Conditionals            | If, For, While, Case, Continue/Break/Pass, Try/Except, Iterables (lambda, enum, filter, zip/chain)             |
| 03_PrintIO                 | Printing, User input, File I/O, I/O module, PrettyPrint, Q                                                     |
| 04_StacksQueues            | Stacks, Queues, Q                                                                                              |
| 05_SearchSort              | LinearSearch, BinarySearch, JumpSearch, InterpSearch, BubbleSort, QuickSort, MergeSort, InsertSort, SelectSort |
| 06_LinkedLists             | LL Construction, LL Ops/Traversal, Q                                                                           |
| 07_BinaryTrees             | BT Construction, BT Ops/Traversal, Q                                                                           |
| 08_Graphs                  | Graph Construction, Graph Ops/Traversal (BFS/DFS), Q                                                           |
| 09_HeapsTries              | Heaps, Tries, Q                                                                                                |
| 10_BitOps                  | Boolean Ops, Bitwise Ops, Bit Math, Bit Shifting, Bit Casting, Q                                               |
| 11_MathTheory              | Algebra, Random, Trigonometry, Random, MatrixOps, Combinatorics, Number Theory, Q                              |
| 12_ObjectOriented          | Class, Function/Partial, Closures, Coroutines, Inheritance, Global, Iterators, Generators, Decorators, Q       |
| 13_Testing                 | Assert, Try, Finally, Except, Speed (Timer, cProfile)                                                          |
| 14_Advanced                | Map/Reduce, Struct, List mutation, Set override, Itertools, Date/Calendar/Time, Q                              |
| ScriptPull                 | Classes: LinkedList, BinaryTree, Graph. Methods: clear_all, cmp, bsearch, qsort                                |
| PracticeQ                  | Useful questions that are neither in the study scripts nor LeetCode                                            |


### Status
| Script            | Content | Syntax | PEP | Questions  | Comments        | 
|-------------------|---------|--------|-----|------------|-----------------|
| 00_CleanCode      | OK      | OK     | OK  | N/A        |                 | 
| 01_DataTypes      | OK      | OK     | OK  | add        |                 | 
| 02_Conditionals   | OK      | OK     | OK  | add        |                 |
| 03_PrintIO        | OK      | OK     | OK  | OK         |                 |
| 04_StacksQueues   | OK      | OK     | OK  | solve      |                 |
| 05_SearchSort     | OK      | OK     | OK  | add        |                 | 
| 06_LinkedLists    | OK      | OK     | OK  | solve      |                 |
| 07_BinaryTrees    | half    | OK     | OK  | solve, inc |                 |
| 08_Graphs         | half    | OK     | OK  | add        |                 |
| 09_HeapsTries     | half    | OK     | OK  | add        |                 |
| 10_ObjectOriented | half    | OK     | OK  | add!       |                 |
| 11_Algorithms     | half    | OK     | OK  | solve      | add Greedy, D&C |
| 12_BitOps         | OK      | OK     | OK  | solve      |                 |
| 13_MathTheory     | half    | OK     | OK  | add        | add num_theory  |
| 14_Testing        | half    | OK     | OK  | add        |                 |
| 15_Advanced       | OK      | OK     | OK  | inc        |                 |
| ScriptPull        | OK      | OK     | OK  | N/A        |                 |
| PracticeQ         | OK      | OK     | OK  | OK         | categorize      |


###
## Manual

<u>Requirements:</u>
* <u>Python</u>: version 3x (3.10 is used)\
* <u>Libraries</u>: Default libs used\
* <u>Inputs</u>: Placed under "./data"

###
Scripts are indented to be executed line-by-line execution.
* Printing ommited most of the time.
* Whitespaces are minimized for better focus and easier scrolling,
* Relevant lines are grouped together as much as possible.
 
###
<u>Study scripts:</u> Focus is comprehension and clarity
* Content is mentioned first 
* Workspace variables are cleared next: 
   ```
   for name in dir():
      if not name.startswith('_'):
         del globals()[name]
   ```
* Then, Content is presented in order
* Finally, relevant questions (that are not in Leetcode) are solved in the end: 
  * Hard Q are omitted and will be covered in AdvancedQ.py in future \
  * LeetCode Q are also omitted since they are covered in [LeetCode](./LeetCode/Leetcode.md) section 
* Remaining basic/medium level Q are solved in PracticeQ.py
   

###
<u>[ScriptPull.py](./ScriptPull.py):</u> Useful classes/methods to utilize in problems and projects.
  * to use classes: ``` from ScriptPull import MyClass ```
  * to use methods: ``` from ScriptPull import * ```
   
###       
<u>Shortcuts used:</u> Although some are common sense, here we go.. <br>
<pre>Q = Question, Ops = Operations, DS = Data Structures, BT = Binary Tree or Binary Search Tree,
LL = Linked List, sol = solution, mod = modification, ans = answer, iter = iterate, concat = 
concatenate, lib = library, func = function, 
</pre>


## License
This project is licensed under the BSD 3-Clause License.
(see the LICENSE.md file for details)

 
