import datetime
# ask the user for three things
def getName():
    n = ''
    while n=='': # keep asking until it is a non-empty string
        n = input('Please enter your name: ') 
    return n

def getAge():
    a = -99
    while a < 0:
        try:
            a_str = input('Please enter your age: ')
            a = int(float(a_str))
        except Exception as e:
            pass
    return a

def getLanguage():
    l = input('Please enter your language: ')
    return l

# combine these into a data structure
def makeStruct(n, a, l):
    # here we build a dictionary
    data = {'name':n, 'age':a, 'language':l}
    return data

def makeString(n, a, l):
    return f'Name: {n} Age: {a} Language:{l}'

# write them to a text file
def writeToFile(user):
    dt = datetime.datetime.today()
    with open('users.txt', 'at') as fout:
        fout.write(user)
        fout.write(f' Date: {dt}')
        fout.write('\n') # nice to put a new line on the end

# read the whole file back
def retrieveData():
    with open('users.txt', 'rt') as fin:
        info = fin.readlines()    
    return info

if __name__ == '__main__':
    n = getName()
    a = getAge()
    l = getLanguage()
    d = makeStruct(n, a, l)
    print(d)
    s = makeString(n, a, l)
    print(s)
    writeToFile(s)
    r = retrieveData()
    print(r)