# We can write data to a file or read data back from a file

def writeToFile(data):
    '''Take some data and write it to a text file'''
    # we need a file access object
    # NB if the file does not exist, Python will ask the OS to create it
    fout = open('data.txt', 'at') # 'w' means (over)write 'a' means 'append' and 't' means 'text
    # we can simply print some text top our file
    print(data, file=fout)
    # its a good idea to close the file access object when we are done
    fout.close()

def readFromFile():
    '''use a file access object to open and red a text file'''
    fin = open('data.txt', 'rt') # 'r' means read 't' means text
    r = fin.readlines()
    print(r)

if __name__ == '__main__':
    # ask the user to enter a name
    n = input('Please enter a name: ')
    # store that name in a text file
    writeToFile(n)
    readFromFile()