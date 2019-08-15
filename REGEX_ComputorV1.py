import sys
import re


# Need to reorganise according to err
def def_errors_dict():
    dictionary = {
        'char': f'Unexpected char, polynomial expression probably false\n',
        'minus': f'Wrong usage of minus (" - "), polynomial expression probably false\n',
        'plus': f'Wrong usage of plus (" + "), polynomial expression probably false\n',
        'equal': f'Wrong usage of equal (" = "), polynomial expression probably false\n',
        'multiplier': f'Wrong usage of multiplier (" * "), polynomial expression probably false\n',
        'xX': f'Wrong usage of " x " or " X ", polynomial expression probably false\n',
        'power': f'Wrong usage of power (" ^ "), polynomial expression probably false\n',
        'dot_1': f'Wrong usage of decimal (" . "), polynomial expression probably false\n',
        'dot_2': f'Wrong usage of decimal(" . "), polynomial expression probably false\n',
        'deg>2': f'Polynomial degree is strictly greater than 2, can\'t solve\n'}

    return dictionary


def check_wrong_model(w_model):
    err = ''
    for wrong in w_model:
        for n, model in enumerate(wrong):
            if model:
                if n == 0:
                    err = 'char'
                elif n == 1:
                    err = 'minus'
                elif n == 2:
                    err = 'plus'
                elif n == 3:
                    err = 'equal'
                elif n == 4:
                    err = 'multiplier'
                elif n == 5:
                    err = 'xX'
                elif n == 6:
                    try:
                        if int(wrong[7]) and int(wrong[7]) > 2:
                            err = 'deg>2'
                        else:
                            err = 'power'
                    except ValueError:
                        err = 'power'
                elif n == 8:
                    err = 'dot_1'
                elif n == 9:
                    err = 'dot_2'

        return err


# Need to reorganise err
def parser(g_model):
    err = 0
    equal = 0
    max_ = 0
    for exp in g_model:
        print(f'exp = {exp}')
        if '=' in exp:
            equal += 1
        for s, e in enumerate(exp):
            if s == 2:
                if int(e) > max_:
                    max_ = int(e)

    if not equal or equal > 1:
        err = 'equal'

    if max_ and not err:
        print(f'Polynomial degree = {max_}')

    return err


if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that !'))

        # Defines the error dictionary
        error = ''
        display_err = def_errors_dict()

        # Format must be "c*x^0 + b*x^1 + a*x^2 = "
        global_model = re.findall(r'''
                                      ([\+\-\=])?                  # Sign if there's one and equal
                                      \s*                          # Spaces
                                      (\d+.\d+|\d+)                # One or more number(s) (float or not) = variables
                                      \s*\*\s*[xX]\s*[\^]\s*       # spaces '*' spaces 'x' or 'X' spaces '^' spaces
                                      (\d+\.\d+|\d+)               # One or more number(s) (float or not) = coefficients
                                    ''', in_put, re.VERBOSE)

        # First try, need to perform more tests => Check for ' " ' at start and end (regex or not ?)
        wrong_model = re.findall(r'''
                                       ([^0-9\+\-\=\. *^xX])         # Catch wrong char
                                       |
                                       ([\-]\s*[^\d ]\s*)            # Delimit the usage of '-' (only figures)
                                       |
                                       ([\+]\s*[^\d xX]\s*)          # Delimit the usage of '+' (figures and xX)
                                       |
                                       ([\=]\s*[^\d \+\-xX]\s*)      # Delimit the usage of '=' (figures, xX, signs)
                                       |
                                       ([\*]\s*[^\d \+\-xX]\s*)      # Delimit the usage of '*' (figures, xX, signs)
                                       |
                                       ([xX]\s*[^\^ \+\-\=]\s*)      # Delimit the usage of 'xX' (pow, signs, equal)
                                       |
                                       ([\^]\s*([^ 0-2])\s*)         # Delimit the usage of '^' (only figures)
                                       |
                                       ([\.][^\d])                   # Delimit the usage of '.' (catches '..')
                                       |
                                       (\d*\.\d+\.\d+)               # Delimit the usage of '.' (catches '1.1.1')
                                    ''', in_put, re.VERBOSE)

        if wrong_model:
            error = check_wrong_model(wrong_model)

        elif global_model:
            print(global_model)
            error = parser(global_model)
        else:
            print(f'It\'s like it\'s not working between me and you...\n\n'
                  f'"{in_put}"\n\n'
                  f'Really ?\n')

        if error:
            print(display_err[error])
