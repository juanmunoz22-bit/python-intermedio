def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Enter a number: "))
    print(divisors(num))
    print('End of file')

if __name__ == '__main__':
    run()