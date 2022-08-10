variable1 = input("input your int number:")
base = input("input base:")
lx = len(variable1)


def function_4base(x, y, i = lx):
    try:
        l1 = list(x)
        l2 = int(x)
        val1 = int(y)
    except ValueError:
        return 'Введено не число. Завершено'

    i -= 1

    if i < 1:
        return l2
    elif i == 1:
        outp = int(l1.pop())
        nextp = int(''.join(l1))
        rem = nextp * val1 + outp
        return rem
    else:
        outp = int(l1.pop())
        nextp = int(''.join(l1))
        rem = nextp * val1 + outp
        n = str(rem)
        last = function_4base(n, y, i)
    return last


print(function_4base(variable1, base))
