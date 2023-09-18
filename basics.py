# comments in Python look like this
# basic mathematics and numbers
a = 3 # this is an integer ( a whole number )
b = 7.2 # this is a floating point number

print(a/b)
print(type(a), type(b)) # we can see what type of data we have

# we can change what a variable is storing
a = -3.333
print(a, type(a)) # -3 float

# Maths: +, -, *, /
# //, % and **
print(5//2) # This is 'modulo' arithmetic - whole-number-division
print(5%2)  # This is 'remainder' division - what's left after integer division
print(5**2) # This raises to the power...

# there are several other data structures
s = 'is it coffee time yet?' # this is a str (a string of characters)
print(type(s))
# we can grab parts of our string like this
# use 'slicing' where the number in square brackets indicates the position of the character
print( s[13] ) # 't' (remember - count from ZERO)
# a string is an ordinal collection of characters, indexed from zero
print( s[6:12] ) # 'coffee' [start:stop-before]
print( s[0:20:2] ) # [start:stop-before:step]
# NB strings are immutable (they cannot be altered once created)
# s[0]='I' # this will FAIL!!!
# but we CAN replace a string with another string
s = 'altered'
print(s)

# here are some more indexed collections
# tuple and list
t = (7, 5.4, 2, a, b, s) # tuples are created using round brackets
# tuple is an immutable ordinal collection of any data type
print(t)
# we can use slicing on a tuple
print( t[2] ) # 2
print( t[4] )
print( t[0:4] ) # 0, 1, 2, 3 members (stop before member at position 4)
# a list is like a tuple except we CAN mutate it
l = [b, s, t, 4, 8.8, 'anything'] # a list is an ordinal collection of mutable members of any data type
print( l )
# we can mutate members of a list
l[2] = 99
print(l)
# we can add members to the list
l.append(t) # this makes t the last member of the list
# we can remove members
l.pop() # the last member is removed
print(l, type(l), type(t))
# for efficiency, use a tuple unless you must have a list
# we can use a loop to iterate over any collection
for i in s:
    print(i) # this iterates over each ordinal member of the collection
for i in l:
    print(i) # each member of the list
for i in t:
    print(i) # each member of the tuple
# there is another collection, called a 'set'
# Set is an ordinal, mutable collection of unique values
my_set = {1,1,1,1,2,2,3,3,6,9} # use curly-brackets to make a set
print(my_set)
# we can use slicing [start:stop-before] and 'add' on sets
# We also have 'boolean' type
# Careful - True evaluates to the same thing as 1 (and a set can only contain unique values)
my_set.add(True) # boolean True (or False)
for i in my_set: # the colon indicates the start iof a block of code
    print(i, type(i))
# when we no longer indent, that is the end of the code block
# NB Python uses 'indentation' for blocks of code