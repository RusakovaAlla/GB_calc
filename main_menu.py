import rational_calc


def start_calc():
    """Меню
    1. выбор вида калькулятора - для рациональных или комплексных чисел
    2. ввод чисел / выражения для обработки
    3. подключение модулей"""

    # global expression

    calc_type = None
    print("Давайте посчитаем! Какой калькулятор вам нужен?")
    while calc_type not in [1, 2]:
        try:
            calc_type = int(input("1 - для рациональных чисел, 2 - для комплексных чисел: "))
        except ValueError:
            print("Повторите ввод типа калькулятора")
            # тут пишем лог
            continue

    if calc_type == 1:
        expression = input("Что считаем? Введите выражение ")
        result = rational_calc.my_eval(expression)
        print(result)
        # тут пишем лог
    else:
        pass  # тут модуль с комплексными числами, как будет реализован ввод - пока не знаю
        # тут пишем лог
