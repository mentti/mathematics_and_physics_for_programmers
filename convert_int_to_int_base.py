variable1 = input("input your int number:")
base = input("input base:")


def function_2base(x, y):
    try:
        val1 = int(x)
        val2 = int(y)
    except ValueError:
        return 'Введено не число. Завершено'

    if val1 < val2:
        return val1
    else:
        outp = val1 % val2
        nextp = (val1 - outp) / val2
        restof = function_2base(nextp, val2)
        vals = []
        vals.insert(0, outp)
        vals.insert(0, restof)
        strVals = [str(v) for v in vals]
        return ''.join(strVals)


print(function_tobase(variable1, base))
