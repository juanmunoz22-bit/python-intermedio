def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Juan', 'lastname': 'Muñoz'}

    super_list = [
        {'firstname': 'Juan', 'lastname': 'Muñoz'},
        {'firstname': 'Pedro', 'lastname': 'Perez'},
        {'firstname': 'Maria', 'lastname': 'Gonzalez'},
        {'firstname': 'Jose', 'lastname': 'Gomez'},
        {'firstname': 'Ana', 'lastname': 'Lopez'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 2.2, 3.3, 4.4, 5.5],
    }

    #for key, value in super_dict.items():
    #   print(key, '-', value)

    for value in super_list:
        print(value['firstname'])

if __name__ == '__main__':
    run()