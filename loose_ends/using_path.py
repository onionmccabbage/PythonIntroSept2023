# by default Python will look in the sytem path for any imports

import sys # sys is the system with python running
# we can add a location where Python should look for library imports
# Careful we may need to 'escape' the '\' character
sys.path.append('D:\\PythonIntroSept2023\\functions')
print(sys.path) # all the locations where Python will look for imports

if __name__ == '__main__':
    import util # this works because we added the new path to find it!!