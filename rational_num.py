def calculator_block(left_num, oper, right_num):
    if oper == '+':
        return sum(left_num, right_num)
    elif oper == '-':
        return sub(left_num, right_num)
    elif oper == '*':
        return mult(left_num, right_num)
    else:
        try:
            return div(left_num, right_num)
        except ZeroDivisionError:
            return "Ошибка деления на 0!"

def sum(left_num, right_num):
    return left_num + right_num

def sub(left_num, right_num):
    return left_num - right_num

def mult(left_num, right_num):
    return left_num * right_num

def div(left_num, right_num):
    return left_num / right_num
