def __color(mode, string, color):
    """
    mode escape sequence code for background or foreground color
    string string to be formatted
    color used color
    """
    if isinstance(color, int):
        escape = "\x1b[{0}8:5:{1}m".format(mode, color)
    elif isinstance(color, tuple):
        r, g, b = color
        escape = "\x1b[{0}8;2;{1};{2};{3}m".format(mode, r, g, b)
    elif isinstance(color, str):
        if not color.startswith('#'):
            try:
                color = int(color)
                return __color(mode, string, int(color))
            except ValueError:
                return string
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        escape = "\x1b[{0}8;2;{1};{2};{3}m".format(mode, r, g, b)
    else:
        return string
    return escape + string.replace("\x1b[0m", '') + "\x1b[0m"


def fg(string, color):
    return __color(3, string, color)


def bg(string, color):
    return __color(4, string, color)


def __format(escape, string):
    """
    Apply desired format
    """
    return "\x1b[{0}m{1}\x1b[0m".format(escape, string.replace("\x1b[0m", ''))


def bold(string):
    return __format(1, string)


def dim(string):
    return __format(2, string)


def italic(string):
    return __format(3, string)


def underline(string):
    return __format(4, string)


def blink(string):
    return __format(5, string)


def invert(string):
    return __format(7, string)


def hide(string):
    return __format(8, string)


def strike(string):
    return __format(9, string)


def double_underline(string):
    return __format(21, string)


def overline(string):
    return __format(53, string)
