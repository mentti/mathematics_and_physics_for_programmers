operation = input("input your opertaion (number symbol number ):")
valid_symbols = ('/', '+', '-', '*')

#def IEEEconverter()
#def summarize()
#def substract()
#def multiply()
#def divide()

def checker(operation, valid_symbols):

    op_list = list(operation)

    if any(sym in operation for sym in valid_symbols):
        pass
    else:
        return 'Type correct operation symbol'

    positions = []

    for i in valid_symbols:
        symbol_pos = operation.find(i)
        positions.append(symbol_pos)

    if sum(positions) > -3:
        return 'Too many operation symbols'

    return positions

checker(operation, valid_symbols)


#def main(operation, valid_symbols):
