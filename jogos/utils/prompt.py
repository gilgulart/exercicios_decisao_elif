import time
import sys
import shutil

WIDTH = shutil.get_terminal_size().columns


def type_text(text, delay=0.05):
    text = text.center(WIDTH)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # print()