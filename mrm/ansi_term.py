"""Module for basic ANSI terminal escape sequences"""

__all__ = ['ESC', 'CURSOR_HOME', 'CLEAR_SCREEN', 'CLEAR_LINE', 'COLOR_RED', 'COLOR_GREEN', 'COLOR_YELLOW', 'COLOR_BLUE', 'COLOR_MAGENTA', 'COLOR_CYAN', 'TEXT_BOLD', 'TEXT_ITALIC', 'TEXT_UNDERLINE', 'TEXT_RESET', 'SAVE_CURSOR', 'RESTORE_CURSOR', 'HIDE_CURSOR', 'SHOW_CURSOR', 'clear_line', 'cursor_home', 'clear_screen', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'bold', 'italic', 'underline', 'save_cursor', 'restore_cursor', 'text_attr', 'hidden_cursor', 'restored_cursor']

from contextlib import contextmanager

ESC = chr(27)

CURSOR_HOME = ESC + '[H'
CLEAR_SCREEN = CURSOR_HOME + ESC + '[2J'
CLEAR_LINE = ESC + '[K'

COLOR_RED = ESC + '[31m'
COLOR_GREEN = ESC + '[32m'
COLOR_YELLOW = ESC + '[33m'
COLOR_BLUE = ESC + '[34m'
COLOR_MAGENTA = ESC + '[35m'
COLOR_CYAN = ESC + '[36m'

TEXT_BOLD = ESC + '[1m'
TEXT_ITALIC = ESC + '[3m'
TEXT_UNDERLINE = ESC + '[4m'
TEXT_RESET = ESC + '[0m'

SAVE_CURSOR = ESC + '[s'
RESTORE_CURSOR = ESC + '[u'

HIDE_CURSOR = ESC + '[?25l'
SHOW_CURSOR = ESC + '[?25h'

def clear_line():
    """Clears current line"""
    print(CLEAR_LINE, end = '')

def cursor_home():
    """Moves cursor to home position"""
    print(CURSOR_HOME, end = '')

def clear_screen():
    """Moves cursor to home position and clears entire screen"""
    print(CLEAR_SCREEN, end = '')

def red(txt):
    """Returns string used to print txt in red"""
    return COLOR_RED + txt + TEXT_RESET

def green(txt):
    """Returns string used to print txt in green"""
    return COLOR_GREEN + txt + TEXT_RESET

def yellow(txt):
    """Returns string used to print txt in yellow"""
    return COLOR_YELLOW + txt + TEXT_RESET

def blue(txt):
    """Returns string used to print txt in blue"""
    return COLOR_BLUE + txt + TEXT_RESET

def magenta(txt):
    """Returns string used to print txt in magenta"""
    return COLOR_MAGENTA + txt + TEXT_RESET

def cyan(txt):
    """Returns string used to print txt in cyan"""
    return COLOR_CYAN + txt + TEXT_RESET

def bold(txt):
    """Returns string used to print txt in bold"""
    return TEXT_BOLD + txt + TEXT_RESET

def italic(txt):
    """Returns string used to print txt in italics"""
    return TEXT_ITALIC + txt + TEXT_RESET

def underline(txt):
    """Returns string used to print txt with underline"""
    return TEXT_UNDERLINE + txt + TEXT_RESET

def save_cursor():
    """Saves current cursor position"""
    print(SAVE_CURSOR, end = '')

def restore_cursor():
    """Restores saved cursor position"""
    print(RESTORE_CURSOR, end = '')

@contextmanager
def text_attr(attr):
    """context manager which sets a text attribute and resets afterwards

    with text_attr(COLOR_RED):
        print('red line 1')
        print('red line 2')
    print('back to white')
    """
    print(attr, end='')
    try:
        yield None
    finally:
        print(TEXT_RESET, end='')

@contextmanager
def saved_cursor():
    """context manager which saves cursor location and restores it afterwards"""
    save_cursor()
    try:
        yield None
    finally:
        restore_cursor()

@contextmanager
def restored_cursor():
    """context manager which restores cursor location and saves it afterwards"""
    restore_cursor()
    try:
        yield None
    finally:
        save_cursor()

@contextmanager
def hidden_cursor():
    """context manager which hides cursor and shows it afterwards"""
    print(HIDE_CURSOR, end = '')
    try:
        yield None
    finally:
        print(SHOW_CURSOR, end = '')