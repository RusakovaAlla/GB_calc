# Блок для расчетов операций с комплексными числами


def Calc_block(left_value, oper, right_value):
    if oper == '+':
        res = sum(left_value, right_value)
    elif oper == '-':
        res = sub(left_value, right_value)
    elif oper == '*':
        res = mult(left_value, right_value)
    else:
        try:
            res = div(left_value, right_value)
        except ZeroDivisionError:
            res = "Ошибка деления на 0!"

    return res


def sum(left_value: complex, right_value: complex):
    return left_value + right_value


def sub(left_value: complex, right_value: complex):
    return left_value - right_value


def mult(left_value: complex, right_value: complex):
    return left_value * right_value


def div(left_value: complex, right_value: complex):
    return left_value / right_value
