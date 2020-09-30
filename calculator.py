"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while calculator = True: 
    input_string = input('>')
    token = input_string.split(' ')
    if token[0] == 'q':
        calculator = False
    else:
        if token[0] == '+':
            add(token[1],token[2])

