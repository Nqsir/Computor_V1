import sys
import re

if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('\nYou\'ll pay for that'))

        # Format must be "c + bx + ax² = "
        general_pattern = re.compile(r'''   ([+,\-,=])?                 # The Sign if there's one
                                    \s*                         # spaces
                                    (\d+.\d+|\d+)               # A number [float or not] that represent a, b or c
                                    \s*\*\s*[xX]\s*[\^]\s*      # spaces * spaces [x or X] spaces ^ spaces
                                    (\d)                        # A number
                                ''', re.VERBOSE)
        model = general_pattern.findall(in_put)
        stars_pattern = re.compile(r'''\*''')
        stars = len(stars_pattern.findall(in_put))
        print(stars)
        error = ''
        equal = 0
        if len(model) != stars:
            print('Nuuuuuuuuuuuuuuuuuuupe')
        elif model:
            print(model)
            for exp in model:
                if '=' in exp:
                    equal = 1
                print(f'exp = {exp}')
                for s, e in enumerate(exp):
                    if s == 2:
                        if int(e) > 2:
                            error = '>2'
                    print(f'e = {e}')
            # for exp in enumerate(model):

            if error or not equal:
                print('Teub !')

        else:
            print(f'It\'s like it\'s not working between me and you... "{in_put}" Really ?')
