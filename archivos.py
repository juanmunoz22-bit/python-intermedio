def read():
    numbers =[]
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Pedro', 'Juan', 'Ana', 'Maria']
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name + '\n')

def run():
    write()


if __name__ == '__main__':
    run()