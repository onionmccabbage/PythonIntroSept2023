# there are many libraries that come with Python
# for random numbers, use the random library
from random import randint # lets us generate a random integer

def makeRandInt():
    return randint(0, 100)

if __name__ == '__main__':
    # loop to make a bunch of random numbers
    for i in range(0,101): # 0-100
        r = makeRandInt()
        if r< 50:
            break # break will stop any loop or while
        print( r )