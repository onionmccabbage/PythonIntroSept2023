# One reason to use Python is it is effectively unlimited
# it will only stop working if it runs out of resources
import sys # sys is a reference to the operating system

def howBig():
    '''Python can deal with any number you might need'''
    print(10**10000)

def getSysParams():
    print(sys.maxsize) # the largest thing that can exist in memory
    print(sys.float_info)

if __name__ == '__main__':
    howBig()
    getSysParams()