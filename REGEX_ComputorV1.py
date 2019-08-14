import sys
import re
from functools import partial


# Need to reorganise according to err
def def_errors_dict():
    dictionary = {'equal': partial(print, f'No "equal" sign or problem with the following coefficient or variable,'
                                          f' polynomial expression probably false'),
                  'n_exp': partial(print, f'Problem with one or more coefficients / variables,'
                                          f' polynomial expression probably false'),
                  'deg>2': partial(print, f'Polynomial degree is strictly greater than 2, can\'t solve'),
                  'power': partial(print, f'Powers must be integer, float detected')}
    return dictionary


# Need to reorganise err
def parser(g_model, s_model):
    print(s_model)
    err = 0
    equal = 0
    max_ = 0
    if len(g_model) != len(s_model):
        err = 'n_exp'
    for exp in g_model:
        print(f'exp = {exp}')
        if '=' in exp:
            equal = 1
        for s, e in enumerate(exp):
            if s == 2:
                try:
                    if int(e) > max_:
                        max_ = int(e)
                    if int(e) > 2:
                        err = 'deg>2'
                except ValueError:
                    err = 'power'
            print(f'e = {e}')

    if not equal:
        err = 'equal'

    if max_ and not err or err == 'degree':
        print(f'Polynomial degree = {max_}')

    return err


if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that !'))

        # Format must be "c + bx + ax² = "
        global_pattern = re.compile(r'''
                                    ([\+, \-, \=])?         # Sign if there's one [+, -, =]
                                    \s*                     # Spaces
                                    (\d+.\d+|\d+)           # One or more number(s) (float or not) = variables
                                    \s*\*\s*[xX]\s*[\^]\s*  # spaces [*] spaces [x or X] spaces [^] spaces
                                    (\d+\.\d+|\d+)          # One or more number(s) (float or not) = coefficients
                                    ''', re.VERBOSE)
        global_model = global_pattern.findall(in_put)
        stars_pattern = re.compile(r'''\*''')
        stars_model = stars_pattern.findall(in_put)

        display_err = def_errors_dict()

        if global_model:
            print(global_model)
            error = parser(global_model, stars_model)
            if error:
                display_err[error]()
                print('Nope !')
            # else:
            #     sys.exit(print('Thumbs up !'))
        else:
            print(f'It\'s like it\'s not working between me and you...\n\n'
                  f'"{in_put}"\n\n'
                  f'Really ?\n')
