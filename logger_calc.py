from datetime import datetime


def result_logger(result):
    current_date = datetime.now()
    current_date_string = current_date.strftime(' %m/%d/%y %H:%M')
    with open('log.csv', 'a', encoding='cp1251') as file:
        file.write(f'{current_date_string}  результат: {result}\n')
