# a range lets us access large amounts of data without that data existing in memory

r = range(-999, 1000, 7) # (start, stop-before, step)
for i in r:
    print(i) # a range will generate the values we need as needed

# if needed, we CAN store the range calues in memory
# careful - this uses more memory than a sample range
t = tuple(r) # tuple uses round brackets
l = list(r)  # list uses square brackets
print(l)