# match is only available in Python 3.10 or better

def main():
    lang = input('What prog language do you like?: ')
    lang = []
    match lang:
        # we can match agaisnt ANYTHING of ANY data type
        case 'Javascript':
            print('You can develop web stuff')
        case 'Python':
            print('You can become a data scientist')
        case 'Java':
            print('You can be a back-end developer')
        case []:
            print('That is an empty list')
        case _: # catches any case we have not yet dealt with
            print('Whatever language, you can solve problems')

if __name__ == '__main__':
    main()