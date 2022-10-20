def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print(f'Choose:\n1 - for working with complex numbers (a + bi)\n2 - for working with rational numbers')
    data_type = get_value()
    if data_type == '1':
        print('Enter first number: ')
        first_value = get_value()
        print('Enter second number: ')
        second_value = get_value()
        print('Select an action (+, -, /, *):')
        action = get_value()
    elif data_type == '2':
        print('Enter first number: ')
        first_value = get_value()
        print('Enter second number: ')
        second_value = get_value()
        print('Select an action (+, -, /, *):')
        action = get_value()
    return (data_type, first_value, action, second_value)