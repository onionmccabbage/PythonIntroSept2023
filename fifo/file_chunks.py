# we can choose to write parts of our data, rather than all of it at once

def writeChunks(t):
    '''write the text to a file in chunks (maybe the data is still arriving)'''
    try: # it is a good idea to hjandle exceptions when dealing with file access
        fout = open('my_words.txt', 'at') # 'at' to append text
        # we can choose the chunk size
        chunk = 24
        # we can measure how much text we have
        size = len(t) # len will always tell us the length of a string of text
        # start from the beginning
        offset = 0
        while True:
            if offset > size:
                # we might choose to put a new line character at the end
                fout.write('\n') # '\n' is the new line character
                fout.close() # close our file output
                break # break out of this loop
            else:
                # slicing: [start:stop-before]
                fout.write( t[offset : offset+chunk] )
                offset += chunk # increment the offset
    except Exception as e:
        print(e)

def readChunks():
    pass

if __name__ == '__main__':
    words = 'here is a long sentence containing a lot of text which we might need to store in a text file to persist while we wait'
    writeChunks(words)
    readChunks()