import logger_calc


def start_calc(calc_type=None):
    print("Какой калькулятор вам нужен?")
    while calc_type not in [1, 2]:
        try:
            calc_type = int(input("1 - для рациональных чисел, 2 - для комплексных чисел: "))
        except ValueError:
            print("Повторите ввод типа калькулятора")
            logger_calc.result_logger(result="Некорректный ввод вида калькулятора")
            continue

    return calc_type


def input_rational():
    global expression
    expression = input("Что считаем? Введите выражение ")
    # тут могут быть ошибки
    return expression


def input_complex():
    nums_to_work = []
    for i in range(1, 4):
        while len(nums_to_work) < 3:
            if i == 3:
                operation = input("Какую операцию производим ")
                nums_to_work.insert(1, operation)
                continue
            else:
                try:
                    a, b = map(float,
                               input(f"Введите через пробел действительную и мнимую части {i} числа ").split(" "))
                    nums_to_work.append(complex(a, b))
                    break
                except ValueError:
                    message = "Некорректный ввод части числа"
                    print(message)
                    logger_calc.result_logger(result=message)
                    continue
                except UnboundLocalError:
                    message = "Отсутствует одна из частей комплексного числа"
                    print(message)
                    logger_calc.result_logger(result=message)
                    continue
                except KeyboardInterrupt:
                    message = "Работа прервана пользователем"
                    print(message)
                    logger_calc.result_logger(result=message)
                    break
    return nums_to_work
