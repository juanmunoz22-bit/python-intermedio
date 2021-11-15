def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Enter a number: "))
        if num < 1:
            raise ValueError("Invalid input. Must be a positive integer")
        print(divisors(num))
        print('End of file')
    except ValueError:
        print('Invalid input. Must be a number')


if __name__ == '__main__':
    run()