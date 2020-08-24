__version__ = '0.1.0'

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from group_project.group_project import GroupProject

def main():
    group_project = GroupProject()
    group_project.on_execute()
