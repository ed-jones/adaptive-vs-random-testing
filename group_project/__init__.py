__version__ = '0.1.0'

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from group_project.window import Window

def main():
    try:
        failure_rate: float = float(input("Enter a failure rate: "))
        assert failure_rate > 0 and failure_rate < 1
    except ValueError:
        print("Failure rate must be a floating point number.")
        exit()
    except AssertionError:
        print("Failure rate must lie between 0 and 1 exclusively.")
        exit()

    window = Window(failure_rate)
    window.on_execute()