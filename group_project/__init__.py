__version__ = '0.1.0'

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from group_project.window import Window

def main():
    window = Window()
    window.on_execute()
