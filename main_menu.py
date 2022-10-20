import logger_calc
import rational_calc
import rational_num
import controls
import calc_complex_numbers

print("Давайте посчитаем!")
calc_type = controls.start_calc()
if calc_type == 1:
    expression = controls.input_rational()
    if len(expression) == 1:
        evaluate = rational_calc.my_eval(expression[0])
    else:
        evaluate = rational_num.calculator_block(*expression)
else:
    expression = controls.input_complex()
    evaluate = calc_complex_numbers.Calc_block(*expression)
try:
    if len(expression) > 1:
        result = f"{str(expression[0]+expression[1]+expression[2])} = {evaluate}"
    else:
        result = f"{str(expression[0])} = {evaluate}"
except TypeError:
    result = f"{expression[0]}{str(expression[1])}{expression[2]} = {evaluate}"
print(result)
logger_calc.result_logger(result=result)
