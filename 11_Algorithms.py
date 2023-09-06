# Contents: Recursion (Backtracking/Memoization),

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var


# -----------------------------------


# -----------------------------------
# Dynamic Programming: Func utilizes itself, needs previous/future results
# Recursion: Func calls itself until it reaches base case, then starts evaluting back
# - Used for sequence generation, when we care about the previous items (opposite of iteration)
# - Maximum recursion depth is 1000 o.w. RecursionError
# - Pros: Wolving complex problems elegantly
# - Cons: Takes time and space, hard to utilize, hard to debug
# Ex: find n!
def fact_iter(n):                       # iterative (standard)
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans

def fact_recr(n):                       # recursive
    if n == 1:                          # base case to stop calling itself
        return 1
    else:
        return n * fact_recr(n-1)       # use previous output (DP)

fact_iter(5)                            # = 120
fact_recr(5)                            # = 120


# Tabulation: top down, save and carry the result(s) downwards
# - Pros: Avoids function recalls
# - Cons: Harder to implement, computes all solutions


# Memoization: bottom up,ncarry the result(s) upwards

# Backtracking: use recursion to explore all possibilities till you get best result


# -----------------------------------
# Greedy: Picks the best sol, hopes local optima = global optima


# -----------------------------------
# Divide and Conquer: Break into simpler subproblems, then combines the solutions


# -----------------------------------
# QUESTIONS
# -----------------------------------
# Algo 01: