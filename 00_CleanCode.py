# Contents: Zen, Indentation, Commentation, Quotation, Spacing (Char/Line), Namespaces, Encoding

# import this: Zen of Python --> Explicit/Flat/Sparse instead of Implicit/Nested/Dense

# Identifiers: No special chars, separate by "_", no starting with digits
# - my_var, my_method, MyClass, MY_CONSTANT --> no My_Constant (ugly)
# - Don't use 'l', 'O', 'I' letters --> confusing
# - Name the exceptions as ***_error


# Indentation: 4spaces over tab, must be consistent throughout the block
# - Python 3 disallows mixing spaces with tabs
# - Don't try to align operators with extra spaces like xyz   = 1
income = (3                            # new line before the operator
          + 4)                         # operator aligned with the 1st input


# Commentation: Should always start with single space
# - Start with capital if full line comment, lowercase if partial line
# - Wrapping at 100 is default but 80 is safer since some applications wrap at 80.


# Quotation: 'chars', 'strings', "special_strings", """"multi_strings""", """docstrings"""
# - For triple-quoted strings, always use double quote chars
print("""She said "hi!" to me.
        Then I said "hi" back to him.""")   # multi-line


# Char Spacing:
# - Surround binary operators with 1 space, ex: a >= b, a and b etc.
# - No space when slice params are omitted, ex: ham[1::3]
# - No space around = when used to indicate a keyword arg or a default, ex: complex(r=real, i=imag)

# Line Spacing:
# - 2 blank lines before/after classes and top function, 1 blank line for methods
# - Try to avoid trailing whitespace anywhere since they are invisible

def myfunc():                           # use self for the 1st arg in instance methods
    """This func is dope."""            # starts with capital, ends with dot


class MyClass:
    """This class is dope."""


print(myfunc.__doc__)
print(MyClass.__doc__)


# Importing: Group and order as standard libs > related 3party libs > local/user libs
# - Order: Module name > docstring > from __future__ > dunders > imports
# -- module dunders are __all__, __version__, __author__ etc.
# - lookup order: current dir > PYTHONPATH > default path


# Namespaces: lookup order is Local > Enclosed > Global > Built-in

# Encoding: Python 2 used ASCII, Python 3 uses UTF-8, other are for testing or foreign chars
