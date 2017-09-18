def func(x, b):
    result = x ** 2 - b
    return result


def d_func(x):
    result = 2 * x
    return result


def Newton(int_value):
    '''(int) -> float
    This function is going to use Newton's methond to get the approximate value
    of square root of the input value.
    the formula for that is x(n) = f(x(n-1))/df(x(n-1)).
    This will return the square root value and result will specify to eight
    decimal places.
    >>> 5
    2.23606798
    >>> 2
    1.41421356
    >>> 3
    1.73205081
    '''
    # decide if the input value is positive or negative
    # x is the starting number to go through Newton's methond
    x = int_value/2
    # define another number which always is next value
    x_1 = 0
    i = 0
    # while loop is going to compute Newton's methond seven times
    while i < 20:
        x_1 = x
        x = x_1 - func(x_1, int_value)/d_func(x_1)
        i += 1
    # get to eight decimal places
    x = round(x, 8)
    return x


def main():
    a = 0
    while a < 1:
        answer = input('Start?\n')
        if(answer == 'yes') or (answer == 'Yes') or (answer == 'y'):
            print(Newton(int(input('Please enter a number:'))))
        else:
            a +=1


#if __name__ == '__main__':
    #main()