import math

def run():
    my_dict = {i: math.sqrt(i) for i in range(1, 1000)}
    print(my_dict)


if __name__ == '__main__':
    run()