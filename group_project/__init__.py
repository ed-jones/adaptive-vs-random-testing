__version__ = '0.1.0'

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

DIMENSIONS = (500, 500)

class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

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
    theApp = App()
    theApp.on_execute()

class App:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = DIMENSIONS
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surface.fill(Colors.WHITE)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.event.get()
        pygame.display.update()

    def on_render(self):
        rect = pygame.Rect(100, 100, 10, 10)
        pygame.draw.rect(self._display_surface, Colors.RED, rect)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
