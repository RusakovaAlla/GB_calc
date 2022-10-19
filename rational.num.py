def calculator_block(data):
    left_num, oper, right_num = data
    if oper == '+':
        return sum(left_num, right_num)
    if oper == '-':
        return sub(left_num, right_num)
    if oper == '*':
        return mult(left_num, right_num)
    if (oper =='/') and (right_num != 0):
        return div(left_num, right_num)
    else:
        return 'Ошибка деления на 0!'

def sum(left_num, right_num):
    return left_num + right_num

def sub(left_num, right_num):
    return left_num - right_num

def mult(left_num, right_num):
    return left_num * right_num

def div(left_num, right_num):
    return left_num / right_num