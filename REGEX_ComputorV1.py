import sys
import re


# Need to reorganise according to err
def disp_errors_dict(err):
    dictionary = {
        'unx': f'Polynomial expression probably false\n\n'
               f'Unexpected \x1b[1;37;41m {err[1]} \x1b[0m\n\n',
        'p_equal': f'Polynomial expression probably false\n\n'
                   f'\x1b[1;37;41m {err[1]} \x1b[0m\n\n not at the end',
        'n_equal': f'Polynomial expression probably false\n\n'
                   f'Unexpected number of \x1b[1;37;41m {err[1]} \x1b[0m\n\n',
        'deg>2': f'Polynomial degree is strictly greater than 2, can\'t solve\n\n'}

    print(f'\n{dictionary[err[0]]}')


def check_wrong_pattern(pattern):
    err_key = ''
    err = []
    for wrong in pattern:
        for n, pat in enumerate(wrong):
            if pat:
                if n == 6:
                    try:
                        if int(wrong[7]) and int(wrong[7]) > 2:
                            err_key = 'deg>2'
                        else:
                            err_key = 'unx'
                    except ValueError:
                        err_key = 'unx'
                else:
                    err_key = 'unx'

                err = pat
                break

        return err_key, err


# Need to reorganise err
def parser(pattern):
    err_key = ''
    err = []
    max_ = 0
    equal = 0
    for exp in pattern:
        if '=' in exp:
            equal += 1
        if int(exp[3]) > max_:
            max_ = int(exp[3])

    if not pattern[-1][0]:
        err_key = 'p_equal'
        err = '='
    elif equal > 1:
        err_key = 'n_equal'
        err = '='

    if max_ and not err_key:
        print(f'Polynomial degree = {max_}')

    return err_key, err


# Complex reduction atm, need to rethink it
def reducing_form(pattern):
    res = []
#     for n, pat in pattern:
#         res.append(pat)
#         if pat[3] == pattern[-1][3]:
#             if pat[1] == '+' or not pat[1]:
#                 if pattern[-1][1] == '+':
#                     res[n][2] = abs(pat[2] - pattern[-1][2])
#         if pat[0] is '=':
#             break
#
    return res


if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that !'))

        error = ''

        # Catches at start and/or end ' or " and replace it
        in_put = re.sub(r'''(^[\"\']|[\"\']$)''', '', in_put, re.VERBOSE)

        print(in_put)

        # Format must be "c*x^0 + b*x^1 + a*x^2 = "
        global_pattern = re.findall(r'''
                                      (\=)?\s*                     # Equal if there's one
                                      ([\+\-])?\s*                 # Sign if there's one
                                      (\d+.\d+|\d+)                # One or more number(s) (float or not) = variables
                                      \s*\*\s*[xX]\s*[\^]\s*       # spaces '*' spaces 'x' or 'X' spaces '^' spaces
                                      (\d+\.\d+|\d+)               # One or more number(s) (float or not) = coefficients
                                    ''', in_put, re.VERBOSE)

        # First try, need to perform more tests => Check for ' " '
        wrong_pattern = re.findall(r'''
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
                                       ([\^]\s*(\d\s*\.|[^ 0-2])\s*) # Delimit the usage of '^' (only int)
                                       |
                                       ([\.][^\d])                   # Delimit the usage of '.' (catches '..')
                                       |
                                       (\d*\.\d+\.\d+)               # Delimit the usage of '.' (catches '1.1.1')
                                    ''', in_put, re.VERBOSE)

        if wrong_pattern:
            error = check_wrong_pattern(wrong_pattern)

        elif global_pattern:
            print(global_pattern)
            error = parser(global_pattern)
            if not error[0]:
                reduced_form = reducing_form(global_pattern)
                # print(f'Reduced form : {}')
        else:
            print(f'It\'s like it\'s not working between me and you...\n\n'
                  f'"{in_put}"\n\n'
                  f'Really ?\n')

        if error[0]:
            disp_errors_dict(error)
