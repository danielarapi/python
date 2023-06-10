# Exercise:
# Write a function that can determine if a number is even or odd
# Verify that input parameter is a valid integer
# Invalid parameters: decimals, negative numbers, non-numeric strings
# Expected output: print if value is odd or even

def even_or_odd(number):
    """
    input: an integer
    action: divide by 2; if remainder is 0 it is even, if 1 it is odd.
    """

    # Verify input is integer
    if (isinstance(number, str) and not number.isnumeric()) or isinstance(number, float):
        print(f'- {number} is not an integer.')
        return None
    else:
        remainder = int(number) % 2
        if remainder == 0:
            print(f'- {number} is even.')
            return 'even'
        else:
            print(f'- {number} is odd.')
            return 'odd'


even_or_odd(10)
even_or_odd(11)
even_or_odd(5.99)
even_or_odd('10')
even_or_odd('11')
even_or_odd('5.99')