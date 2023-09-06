# Cntent: Class, Function, Partial Function, Operator Overload, Closures, Coroutines, Inheritance,
         # Global, Iterators, Generators, Decorators, Q

for name in dir():
    if not name.startswith('_'):
        del globals()[name]


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

        
       
            