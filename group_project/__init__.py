__version__ = '0.1.0'

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from group_project.group_project import GroupProject

def main():

    # Get failure area from stdin
    try:
        failure_rate_string: str = input("Enter a failure rate: ")
        failure_rate = float(failure_rate_string)
        assert failure_rate > 0 and failure_rate < 1
    except ValueError:
        if failure_rate_string == '':
            print("No failure rate supplied, using 0.01 as default")
            failure_rate = 0.01
        else:
            print("Failure rate must be a floating point number.")
            exit()
    except AssertionError:
        print("Failure rate must lie between 0 and 1 exclusively.")
        exit()

    group_project = GroupProject(failure_rate)
    group_project.on_execute()