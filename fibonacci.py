sequence = [0]

def fibonacci(maximum, first = 0, second = 1):
    if second <= maximum:
        sequence.append(second)
        first, second = second, first + second
        fibonacci(maximum, first, second)
    
    return sequence

if __name__ == "__main__":
    print('Fibonacci Sequence')
    print('=' * 18)
    print()
    print('What is the maximum number in the sequence you would like to return?')
    print('Be careful in entering a number too large or the system may error.')
    maximum = int(input('Maximum value:  '))

    if maximum >= 0 and isinstance(maximum, int):
        sequence = fibonacci(maximum)
        print(sequence)
    else:
        print('Invalid input, maximum must be a positive integer.')
    

    
    

