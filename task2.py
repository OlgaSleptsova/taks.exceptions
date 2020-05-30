s = input()
lst = s.split()

try:
    assert len(lst) == 3, 'Количество аргументов передано не верно'
    assert lst[0] in ('+', '-', '*', '/'), 'операция не доступна'
except Exception as e:
    print(e)


def summa(syll):
    summ = int(syll[1]) + int(syll[2])
    return summ


def subtrac(sub):
    subt = int(sub[1]) - int(sub[2])
    return subt


def multiplic(mul):
    multi = int(mul[1]) * int(mul[2])
    return multi


def division(div):
    try:
        divis = int(div[1]) / int(div[2])

    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    else:
        return divis


def polish_notation(y):
    if y[0] == '+':
        print(summa(y))
    elif y[0] == '-':
        print(subtrac(y))
    elif y[0] == '*':
        print(multiplic(y))
    elif y[0] == '/':
        print(division(y))


polish_notation(lst)