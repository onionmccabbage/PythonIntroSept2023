# match is only available in Python 3.10 or better

def main():
    lang = input('What prog language do you like?: ')
    match lang:
        case 'Javascript':
            print('You can develop web stuff')
        case 'Python':
            print('You can become a data scientist')
        case 'Java':
            print('You can be a back-end developer')
        case _:
            print('Whatever language, you can solve problems')

if __name__ == '__main__':
    main()