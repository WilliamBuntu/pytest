def main():
    x = int (input('What is the value of x : '))
    print(f'the square root of {x} is ', square(x) )


def square(x):
    return x + x

if __name__ == '__main__':
    main()
