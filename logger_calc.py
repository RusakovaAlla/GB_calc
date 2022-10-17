from datetime import datetime as dt
from time import time


def result_logger(time, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} результат :{}\n'.format(
            time, result))
