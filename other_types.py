# in addition to set, tuple, list, string, in and flaot there are other types
# boolean
b = True
c = False
# None
d = None # represents nothing!!
print(b, c, d, type(b), type(c), type(d))
# There is another collection, called a dictionary
# dictionary is a NON-INDEXED mutable colection of name:value pairs
users = {'usrM':'Ethel', 'usrN':'Briony', 'usrP':'Con'}
print( users['usrP'] ) # the members of a dictioanry are NOT indexed by number
# we can iterate over a dictionary
for k,v in users.items(): # we need to specify items so we can iterate
    print( k, v )

print( type(users) ) # dict
# we can mutate members
users['usrN'] = 'Timnit'
# we can add new members to the dict
users['usrQ'] = 'Ed'
print(users)