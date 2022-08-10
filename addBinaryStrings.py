variable1 = input("input your first int number:")
variable2 = input("input your second int number:")


def addBinaryStrings(x, y):
    output = []
    carryDigit = '0'

    for i in range(len(x)):
        k1 = x[i]
        k2 = y[i]
        if k1 == k2:
            writeDigit = carryDigit
            carryDigit = k1
        else:
            writeDigit = '1'
        output.insert(0, writeDigit)
    if carryDigit == '1':
        output.insert(0, '1')
    return ''.join(output)


print(addBinaryStrings(variable1, variable2))
