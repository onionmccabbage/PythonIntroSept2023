def prettyPrint(n):
    output = ''
    for k,v in n.items():
        output += f'{k} contains {v}\n'
    return output