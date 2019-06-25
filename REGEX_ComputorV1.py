import sys
import re

if __name__ == '__main__':
    while True:
        try:
            in_put = input('Please enter your polynomial expression : ')
        except KeyboardInterrupt:
            sys.exit(print('You\'ll pay for that'))

        # Format must be "c + bx + ax² = "
        pattern = re.compile(r'''   ([+,\-,=])?                 # The Sign if there's one
                                    \s*                         # spaces
                                    (\d+.\d+|\d+)               # A number [float or not] that represent a, b or c
                                    \s*\*\s*[xX]\s*[\^]\s*      # spaces * spaces [x or X] spaces ^ spaces
                                ''', re.VERBOSE)
        model = pattern.findall(in_put)
        if model:
            print(model)
            # for exp in enumerate(model):

        else:
            print(f'It\' like it\'s not working between me and you... {in_put} Really ?')
