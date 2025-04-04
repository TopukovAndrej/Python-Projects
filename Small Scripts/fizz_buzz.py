for i in range(1, 101):
    isDivisibleByThree = i % 3 == 0
    isDivisibleByFive = i % 5 == 0

    if isDivisibleByThree and isDivisibleByFive:
        print('FizzBuzz')
    elif isDivisibleByThree:
        print('Fizz')
    elif isDivisibleByFive:
        print('Buzz')
    else:
        print(i)