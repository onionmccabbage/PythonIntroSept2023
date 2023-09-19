def checkValidInt(i):
    if type(i)==int or i.isdigit():
        return int(float(i))
    else:
        return 0