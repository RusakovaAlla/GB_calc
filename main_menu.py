import logger_calc
import rational_calc
import controls
import calc_complex_numbers

print("Давайте посчитаем!")
calc_type = controls.start_calc()
if calc_type == 1:
    expression = controls.input_rational()
    evaluate = rational_calc.my_eval(expression)
else:
    expression = controls.input_complex()
    evaluate = calc_complex_numbers.Calc_block(*expression)

result = f"{str(expression)} = {evaluate}"
print(result)
logger_calc.result_logger(result=result)
