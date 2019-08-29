import sys
import re


# Need to reorganise according to err
def disp_errors_dict(err):
    dictionary = {
        'unx': f'Polynomial expression probably false\n\n'
               f'Unexpected \x1b[1;37;41m {err[1]} \x1b[0m\n\n',
        'p_equal': f'Polynomial expression probably false\n\n'
                   f'\x1b[1;37;41m {err[1]} \x1b[0m\n\n not associated to the last term or last term is false',
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
    reduced = []
    for pat in pattern:
        reduced.append(list(pat))
        if pat[0] is '=':
            break
        elif pat[3] == pattern[-1][3]:
            if pat[1] != pattern[-1][1]:
                reduced[-1][2] = round(float(pat[2]) + float(pattern[-1][2]), 1)
            else:
                reduced[-1][2] = round(float(pat[2]) - float(pattern[-1][2]), 1)

            if reduced[-1][2] < 0:
                reduced[-1][1] = '-'
                reduced[-1][2] = abs(reduced[-1][2])

    reduced.__delitem__(-1)

    res = ''
    for r in reduced:
        res += f' {r[1]} {r[2] if float(r[2]).is_integer() else float(r[2])} ^ {r[3]}'
    print(f'Reduced form:{res} = 0')
    return reduced


if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that !'))

        error = ['', '']

        if in_put.upper() == 'EXIT' or in_put.upper() == 'EXIT()':
            sys.exit(print('\nYou\'ll pay for that !'))

        # Catches at start and/or end ' or " and replace it
        in_put = re.sub(r'''(^[\"\']|[\"\']$)''', '', in_put, re.VERBOSE)

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
