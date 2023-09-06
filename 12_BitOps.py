# Contents: Boolean Ops, Bitwise Ops, Bit Math, Bit Shifting, Bit Casting, Questions

for var in dir():
    if not var.startswith('_'):
        del globals()[var]
del var


# -----------------------------------
# Boolean Literals
bool(-2)                                # = True, only 0 is False
not(False or True)                      # = not True = False, boolean (logical) op
2 in [1, 2, 3]                          # = True, there exists or not
False + True + 5                        # = 0+1+5 = 6, boolean literals, OR-like
2 != 4 > 2                              # = (2 != 4) AND (4 > 2) = TRUE
all([1, 0, 1])                          # = False, AND operation
any([False, True, False])               # = True, OR operation
print(any([]), all([]))                 # = False, True

# 2's complement
~0                                      # = inv(b00) = b11 = -1, bitwise op (2's complement)
~1                                      # = inv(b01) = b10 = -2 = operator.xor_(0, 1)
print(0 < a >= b)                       # = (0 < a) AND (a >= b) = TRUE (doesn't check for 0 < b)

a = b = 1; a is b                       # = True, same memory location (pointer to 1)
a = b = [1,2,3]; a is b                 # = False, different memory allocations for arrays


# -----------------------------------
# Bitwise Ops
bin(0b0110 + 0b0010)                    # gives int by default, so need to cast
bin(0b0110 + 0b0101)                    # = 0001
bin(0b0011 - 0b0010)                    # = 0001
bin(0b0110 - 0b0011)                    # = 0011
bin(0b1000 - 0b0110)                    # = 0010
bin(0b0011 * 0b0101)                    # = 0011 + 100 + 1000 = 1111
bin(0b0011 * 0b0011)                    # = 0110
bin(0b1101 ^ 0b0101)                    # = XOR = 1000
bin(0b1101 ^ 0b0101)                    # = OR = 1000
bin(0b0100 * 0b0011)                    # = 1100 (4x = by 2)

# -----------------------------------
# Bit Shifting
x = 5   # = 101 (3 bits)
    # Arihmetic shift (>>): keeps the sign bit (MSB)
    # Logical shift (>>>): push a 0 on the left (MSB)
    # x >>> 1  # = 0+10 = 2     --> no logical shift in Python
x >> 1  # 101 >> 010 = 3 but Python only has Logical shift with but prefers unsigned
# if you logical shift a negative number too much it'll be -1-1-1... = -1 signed int

bin(0b1101 >> 2)        # = push 0s on left: --> 0110 --> 0011
~x  # = -(x+1) = -6 --> assumes signed (2s comp) --> 
def bit_not(x, num_bits):  # deals with unsigned (invert each bit)
    return (1 << num_bits) - 1 - x  # get 1000-1 = 111 and subtract x from 111
bit_not(x, 3)   # = 010 = 0b10 = 2
bin(0b1101 ^ bit_not(0b1101, 4))   # 1101 XOR 0010 = 1111
bin(1011 & (bit_not(0, 1) << 2))   # = 1011 and 0100 = 0000 --> Gayle says 1000?


# -----------------------------------
# Bit Casting:
char1 = '4'; int1 = 11; int2 = 3; str1 = "101"
type(char1)  # type of both char and string is str
i = ord(char1)       # = 4
b = int(str1, 2)     # = 5
f = float(str1)      # = 101.0
h = hex(int1)        # = 0xb
c = complex(int1, int2)
s = str(int1)        # "int1"
print("i=%, b=%, f=%, h=%, c=%, s=%", i,b,f,h,c,s)

a = 'asd'; b = b'asd'   # string and variables are case sensitive, bytes are not
c = a.encode('ASCII')   # string to byte, via ascii or utf-8  --> c=b
d = c.decode('ASCII')   # decode back to string --> d=a


# -----------------------------------
# QUESTIONS
# -----------------------------------
# BitOps 01: Function to get the i-th bit
x = 5

# Sol:
def getbit(x, i): 
    flag = 0b1 << i   # = 0b10 = 2
    if (x & flag) == flag : # 6 & 2 = 2 in bit style
        return 1
    else :
        return 0  
bin(x)
getbit(x, 0)    # 0101 --> 1


# -----------------------------------
# BitOps 02: Function to get 2's Complement
# Given same --> 5's complement is -6

# Sol:
def comp2(x):
    n = bin(x).bit_length() - 1
    xb = bin(2**(n-1) + x)
    res = xb + bin(2**(n-1)) # 101 + 1000 = 1101    
    return res
comp2(x)
    

# -----------------------------------
# BitOps 03: Count the set bits (1s) of an integer
x = 5   # 2
# Sol:
def count_highs(x):
    arr = bin(x)
    cnt = 0
    for i in range(len(arr)) : 
        if arr[i] == '1': 
            cnt += 1
    return cnt        
count_highs(x)


# -----------------------------------
# BitOps 04: Count total set bits in all numbers from 1 to n
n = 5   # 1 + 1 + 2 + 1 + 2 = 7

# Sol 1: utilize count_highs, O(n^2)
count = 0
for i in range(n+1) : 
    count += count_highs(i)
    #print(count)
count    

# Sol 2: 00, 01, 10, 11, 100, 101 ... --> LSB toggles every 2^0 bits, 1st bit toggles every 2^1 bits


# -----------------------------------
# BitOps 05: Find the number of bits you would need to flip to convert an integer
# Given:
a = 0b1011101  # = 29
b =    0b1111  # = 15 --> 3 bits

# Sol 1: XOR and count 1s
count_highs(a ^ b)

# Sol 2: O(k*n)
cnt = 0 
a_bin = bin(a)
b_bin = bin(b)
aa = a_bin[2: ]
bb = b_bin[2: ]
na, nb = len(aa), len(bb)
for i in range(min(na, nb)):
    if aa[i] != bb[i] :
        cnt += 1
if nb > na :
    for i in range(na+1, nb) :    
        if bb[i] == 1 : 
            cnt = cnt + abs(nb - na)    
elif na > nb :
    for i in range(nb+1, na) :  
        print(aa[i])
        if aa[i] == 1 : 
            cnt = cnt + abs(na - nb)   
cnt


# -----------------------------------
# BitOps 06: Rotate bits of a number
# Q: direction? --> show both
x = 0b10000
i = 3
rotation = 'right'

# Sol: 
n = len(list(bin(x))) - 2
if rotation == 'left' : 
     res = (x << i | x >> (n-i) ) & (2**n-1)  # need to & with [11111] o.w. left shifts overflow
elif rotation == 'right' : 
    res = x >> i | x << (n-i)  & (2**n-1)  
else :
    print("wrong rotation")
bin(res)


# -----------------------------------
# BitOps 07: Swap odd/even bits in an integer with minimal instructions (bit0vs1, bit2vs3 ..)
# Given:
c = 0b10001  # 0b  0001

# Sol: Mask evens/odds with 0xAA/0x1, then shift, then merge with OR 
evens = c & 0x55
bin(evens)
odds = c & 0xAA
bin(odds)
c_swapped = bin( (evens << 1) | (odds >> 1) )


# -----------------------------------
# BitOps 08: Find the years that your money will exceed Bobs when you double every year
# Given:
bills_money = 50 * 10**9  # 2^32 = 4GB = 4B --> *2^4 = 64GB > 50GB
my_money = 1

# Sol: 
years = 0
while my_money < bills_money :
    my_money = 2*my_money
    years = years + 1
print("After %d years, my money will be %d" % (years, my_money) )


# -----------------------------------
# BitOps 09: Function for decimal to binary conversion
# Q: check for decimal? --> no
# Given:
x = 14       # bits = 1110

# Sol 1: div by 2 and check if > 0
bits = 0b0
q = x
pwr = 0
while q > 1 :
    r = q % 2
    if r == 1:
        bits = bits + (0b1 << pwr)
    #else:
    #    bits = bits + 0b0 << pwr # no need if next iters bring shifted 1... + bits
    q = q // 2
    print(q, r, bin(bits))
    pwr = pwr + 1
    if q == 1:
       bits = bits + (0b1 << pwr)       
bin(bits)

# Sol 2: Recur
bits = []
def dec2bin(n):
    if n > 1 :
        dec2bin(n // 2)      # divide all the way first till bottom
    bits.append(n%2)        # collect remainders from bottom to top    
    return bits
dec2bin(x) 
    
 
# -----------------------------------
# BitOps 10: Function for binary to decimal conversion
# Q: result in array? --> yes       prefix 0s needed? --> no
# Given: 
bits = 1110        # x = 14
 
 # Sol:
pwr = 0
q = bits
x = 0
while q > 0 :
    r = q % 10
    x = x + r*(2**pwr)
    q = q // 10
    print(q, r, x)
    pwr = pwr + 1
x
 
 
# -----------------------------------
# BitOps 11: Find max consecutive 1s with flipping m zeros --> FIX
# Q: or Which m bits to flip 
    # m can be 0? --> no
# Given:
bits = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]    # sol: flip the 2nd 0 --> best_n = 8
n = len(bits)
m = 1

# Sol: Sliding window, maintain the window with at most m zeros inside
best_win = []
best_n = 0
zeros = set()
i,j = 0, 0
while (i <= j) and (j < n):
    print(i,j, zeros, best_win)
    if (bits[j] != 0) and (j != n-1) :    # proceed j till a zero encounter 
        j = j + 1                   # assume n-th bit is a wall, so assume 0 after that
    else:    # zero encounter
        if j not in zeros :     # new zero
            print("zero encountered")
            zeros.add(j)    # add the zero index as a set
            if len(zeros) > m :  # overflow, record the window and proceed i to unload prev 0s
                win = bits[i:j]  # means j-1 anyway
                if len(win) > best_n :  # record if best
                    best_win = win
                    best_n = len(win)
                i = i + 1
                if bits[i-1] == 0 :
                    print("zero unloaded")
                    zeros.remove(i-1)       # unload an earlier zero from the set
                    j = j + 1   # not that we got rid of 1 zero, we can continue inc j
                
        #else : # zeros <= m :
         #   j = j + 1                                               
best_win


# -----------------------------------
# BitOps 12: Debugger, explain what the following code does: (n & (n-1)) == 0
# Q: 
# Given:
# Sol: n and n-1 never share a 1
# n - 1 = abc100 - 1 = abc001 --> abc100 & abc001 = 0 --> abc = 0 --> n = 100 = 2^3
# so checks if the number is a power of 2

   
# -----------------------------------
# BitOps 13: Find the maximum subarray XOR in a given array    
# Q: 
# Given:
arr = [8, 1, 2, 12, 7, 6]
n = len(arr)

# Sol 1: 2 XOR loops, O(n^2)/O()
best = -2147483648      # max xor result 
for i in range(n):      # subarray from i to j 
    curr_xor = 0        # to store xor of current subarray 
    for j in range(i, n):       
        curr_xor = curr_xor ^ arr[j]
        if curr_xor > best :
            sub = arr[i:j+1]
            best = curr_xor
sub     # best subbarray
best    # xor value
    

# -----------------------------------
# BitOps 14: Find the element that appears once, where every element occurs 3x except one 

arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]   # out = 1

# Sol 1: Sort and check if different than previous one, O(nlogn)/O(1)
# Sol 2: Hash counts and seek cnt==1, O(n)/O(n)
# Sol 3: Bits, O(n)/O(1)
 # ‘ones’ and ‘twos’ are initialized as 0. For every new element in array,
 # find out the common set bits in the new element and previous value of ‘ones’.
 # These common set bits are actually the bits that should be added to ‘twos’.
 # So do bitwise OR of the common set bits with ‘twos’. ‘twos’ also gets some extra bits
 # that appear third time.
def unique_int(arr):
    ones = 0
    twos = 0
    for x in arr:
        twos |= ones & x            # bits that appeared 2nd, 5th, 8th time etc.
        ones ^= x                   # bits that appeared 1st, 4th, 7th time...
        not_threes = ~(ones & twos)     # bit mask
        ones &= not_threes          # remove bits appearing 3rd time
        twos &= not_threes
    return ones
unique_int(arr)
    
                       
# -----------------------------------
# BitOps 15: Find nth Magic Number, is sum of unique powers of 5
# Q: negative powers? --> no
n = 5   # -> 5, 25, 25+5, 125, 125+5, 125+10 ..

# Sol: Treat it like base 5 except LSB is 5^1, not 5^0
def nthMagicNo(n):  # 101 -> 5^3 + 5^1= 125 + 5 = 130
    pwr = 1
    answer = 0    
    while n:          # for each bit
        pwr = pwr*5         
        if n & 1:     # if last bit of n is set
            answer += pwr        
        n >>= 1         # check next LSB or n = n/2       
    return answer 
nthMagicNo(n)


# -----------------------------------
# BitOps 16: Draw a horizontal line from x1 to x2  --> FIX
    # 1 byte stores 8 consecutive pixels, w = 8*x
# Sol: # black squares = white squares, c
def drawLine(screen, width, x1, x2, y):  # set x1 to x2 btyes to 111.. = 0xFF
    offset = x1 % 8
    byte_start = x1 / 8
    if start_offset != 0:
        byte_start += 1
                
    end_offset = x2 % 8
    byte_end = x2 / 8
        
    if end_offset != 7:
        byte_end -= 1

    # Set full bytes
    for b in range(byte_start, byte_end + 1):
        screen[(width / 8) * y + b]  # = #(byte) 0xFF
   # Create masks for start and end of line
   # byte_start_mask = (byte) (0xFF >> start_offset)
   # byte_end_mask = (byte) -(0xFF >> (end_offset + 1))

    # Set start and end of line
    # if (xl / 8) == (x2 / 8):    # x1 and x2 are in the same byte

        # byte_mask= (byte) (start_mask & end_mask)
        # screen[(width / 8) * y + (xl / 8)] I= mask
    #else:
        # if start_offset != 0:
            # byte_number =(width/ 8) * y + byte_start - 1
            # screen[byte_number] |= start_mask
    
    if end_offset != 7:
        byte_number =(width/ 8) * y + byte_end + 1
        screen[byte_number] |= end_mask

    return


# -----------------------------------
# BitOps 16: Find Next Sparse Number, that's >=n
# Q: sparse # is no two adjacent 1s in its binary representation
# Given: Don't use n for constants (non-arrays) --> will confuse the big O
x = 5  # --> 6 --> 7 --> 8 yes  
# 010 --> 010 --> 0101 --> 0101 --> 1000 --> 1001 --> 1010
#  1  --> 2   -->  4   --> 5    --> 8    --> 9    --> 10

# Sol1: Write isSparse O(logx) and recur till it returns true, O(xlogx) since x <sol < 2x
# Sol2: Form a binary array

# -----------------------------------
# BitOps 17: Sum of bit differences among all pairs

# Sol: 

    
# -----------------------------------
# BitOps 18: Convert a RGB Color (three 1-byte numbers) to a 6-digit Hex String --> FIX
# Given:
rgb = []
hexx = String.format("#%02x%02x%02x", r, g, b)
