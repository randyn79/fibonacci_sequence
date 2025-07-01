#!/usr/bin/env python3

def fibonacci(maximum):
    sequence = []
    first, second = 0, 1
    while first <= maximum:
        sequence.append(first)
        first, second = second, first + second
    return sequence

if __name__ == "__main__":
    print('Fibonacci Sequence')
    print('=' * 18)
    print()
    print('What is the maximum number in the sequence you would like to return?')
    print('Be careful in entering a number too large or the system may error.')
    try:
        maximum = int(input('Maximum value:  '))
        if maximum >= 0:
            sequence = fibonacci(maximum)
            print(sequence)
        else:
            print('Invalid input, maximum must be a positive integer.')
    except ValueError:
        print('Invalid input, please enter a valid integer.')
