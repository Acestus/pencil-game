name = input()

def normalize(name):

    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('ë', 'e')
    name = name.replace('å', 'aa')
    name = name.replace('œ', 'oe')
    name = name.replace('æ', 'ae')
    new_name = name

    return new_name

print(normalize(name))