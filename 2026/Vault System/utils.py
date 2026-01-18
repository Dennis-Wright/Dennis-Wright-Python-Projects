import os

def get_width():
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80

    return width
# End function

def get_padding(terminal_width, text):
    left_padding = max((terminal_width - text) // 2, 0)

    return left_padding
