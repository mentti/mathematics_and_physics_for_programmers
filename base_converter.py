variable = input("input your number:")
base1 = input("input number base (2 to 16):")
base2 = input("input base you want to get (2 to 16):")


def convertBase(variable, base1 = '10', base2 = '10'):

    # for letters removing
    decodeDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # checking part
    codeString = '0123456789ABCDEF'

    try:
        b1 = int(base1)
        b2 = int(base2)
    except ValueError:
        return 'Система счисления должна быть числом'

    if b1 < 2 or b1 > 16 or b2 < 2 or b2 > 16:
        return 'Указана недопустимая база'

    for letter in variable:
        if letter not in codeString[:b1]:
            return 'Число не соответствует базе или указано не верно'

    # main part
    lst1 = list(variable)
    lenlst1 = len(lst1)
    tenth = 0

    # remove letters and convert into 10th
    for i in range(0, lenlst1, 1):
        lst1[i] = decodeDict.get(lst1[i])
        tenth = tenth + (lst1[i] * (b1 ** (lenlst1 - 1 - i)))

    # convert from 10th to base

    def innerConvert(tenth, base):
        vals = []
        while tenth > base:
            rem = tenth % base
            vals.insert(0, rem)
            tenth = tenth // base
        vals.insert(0, tenth)
        return vals


    result = innerConvert(tenth, b2)


    # convert to letters
    lenlst2 = len(result)

    for l in range(0, lenlst2, 1):
        result[l] = list(decodeDict.keys())[list(decodeDict.values()).index(int(result[l]))]

    return ''.join(result)

print(convertBase(variable,base1,base2))


