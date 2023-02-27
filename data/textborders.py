from colorama import Fore, Style
import textwrap


def maintext(text):
    print('{:-^70}'.format(text.upper()))

def maintext_system(text):
    print(Fore.RED + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)

def maintext_system_l(text):
    print(Fore.LIGHTRED_EX + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)


def maintext_system_g(text):
    print(Fore.LIGHTGREEN_EX + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)


def maintext_system_c(text):
    print(Fore.CYAN + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)


def maintext_system_cl(text):
    print(Fore.LIGHTCYAN_EX + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)

def maintext_system_grats(text):
    print(Fore.LIGHTYELLOW_EX + '{:-^70}'.format(text.upper()))
    print(Style.RESET_ALL)


def lefttext(text):
    print('{:<70}'.format(text))

def lefttext_system(text):
    print(Fore.RED + '{:<70}'.format(text))
    print(Style.RESET_ALL)
def lefttext_system_rl(text):
    print(Fore.LIGHTRED_EX + '{:<70}'.format(text))
    print(Style.RESET_ALL)
def lefttext_system_l(text):
    print(Fore.LIGHTRED_EX + '{:<70}'.format(text))
    print(Style.RESET_ALL)

def lefttext_system_g(text):
    print(Fore.GREEN + '{:<70}'.format(text))
def lefttext_system_gl(text):
    print(Fore.LIGHTGREEN_EX + '{:<70}'.format(text))


def lefttext_system_c(text):
    print(Fore.CYAN + '{:<70}'.format(text))
def lefttext_system_cl(text):
    print(Fore.LIGHTCYAN_EX + '{:<70}'.format(text))
def lefttext_system_m(text):
    print(Fore.MAGENTA + '{:<70}'.format(text))
def lefttext_system_ml(text):
    print(Fore.LIGHTMAGENTA_EX + '{:<70}'.format(text))
def lefttext_system_grats(text):
    print(Fore.YELLOW + '{:<70}'.format(text))
def lefttext_system_grats_l(text):
    print(Fore.LIGHTYELLOW_EX + '{:<70}'.format(text))




# right-justify print
def righttext(text):
    print('{:>70}'.format(text))

def righttext_system(text):
    print(Fore.RED + '{:>70}'.format(text))
    print(Style.RESET_ALL)

def righttext_system_l(text):
    print(Fore.LIGHTRED_EX + '{:>70}'.format(text))
    print(Style.RESET_ALL)


def righttext_system_g(text):
    print(Fore.GREEN + '{:>70}'.format(text))
def righttext_system_gl(text):
    print(Fore.LIGHTGREEN_EX + '{:>70}'.format(text))


def righttext_system_c(text):
    print(Fore.CYAN + '{:>70}'.format(text))


def righttext_system_cl(text):
    print(Fore.LIGHTCYAN_EX + '{:>70}'.format(text))


# centered print

def centertext(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print('{:^70}'.format(line))

def centertext_system(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.RED + '{:^70}'.format(line))
        print(Style.RESET_ALL)
def centertext_system_l(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.LIGHTRED_EX + '{:^70}'.format(line))
        print(Style.RESET_ALL)

def centertext_system_g(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.GREEN + '{:^70}'.format(line))
        print(Style.RESET_ALL)
def centertext_system_gl(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.LIGHTGREEN_EX + '{:^70}'.format(line))
        print(Style.RESET_ALL)
def centertext_system_c(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.CYAN + '{:^70}'.format(line))
        print(Style.RESET_ALL)

def centertext_system_cl(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.LIGHTCYAN_EX + '{:^70}'.format(line))
        print(Style.RESET_ALL)

def centertext_grats(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.LIGHTYELLOW_EX + '{:^70}'.format(line))
        print(Style.RESET_ALL)
def centertext_blue(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.BLUE + '{:^70}'.format(line))
        print(Style.RESET_ALL)
def centertext_blue_l(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        print(Fore.LIGHTBLUE_EX + '{:^70}'.format(line))
        print(Style.RESET_ALL)

def gridoutput(dict_data):
    basestring = '{: '
    centerchar = ['^']
    cap = '} '
    rowformat = ''
    columwidth, thedata, dataheader = [], [], []
    for key, value in dict_data.items():
        dataheader.append(key)
        thedata.append(value)
        columwidth.append(len(max([str(key), str(value)], key=len)))
    for i, widthsize in enumerate(columwidth):
        rowformat += basestring
        rowformat += centerchar[i % len(centerchar)]
        rowformat += str(widthsize)
        rowformat += cap
    maintext_system_cl(('{' + dict_data['Name'] + '}').upper())

    # a hacky way to center the text after the formatting is done
    spacesqty = (70 - len(rowformat.format(*dataheader))) / 2
    spaces = ' ' * int(spacesqty)
    print(Fore.LIGHTBLUE_EX + spaces + rowformat.format(*dataheader))
    print(Fore.LIGHTWHITE_EX + spaces + rowformat.format(*thedata))

def lr_justify(left, right, width):
    return '{}{}{}'.format(left, ' ' * (width - len(left + right)), right)