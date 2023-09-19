# data structures let us decide where to store data
# problem - we need to remember number, words
a = 150972
b = "ah now I recall"
running = True

# problem - we need to remember lots of stuff
pins = [3456, 8701, 1100, 3264] # a list
pins.append(7652) # remember this one as well

# if we know the stuff will not change, then use a tuple
shopping = ('apples', 'pears', 'banana', 'durian')

# if you need to make sure the collection contains only unique stuff, use a set
quiz_members = {'Ada', 'Beatie', 'Cathy', 'Deidre', 'Ada'}
print(quiz_members)
print(a) # only unique members

# sometimes ordinality is irrelevant. We prefer labels (or keys)
dict_en = {
    'python':'a snake, a british commedy and a language',
    'Java':'A country, a coffee and a language'
    }
