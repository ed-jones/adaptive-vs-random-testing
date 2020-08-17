import pygame
from pygame.locals import *

DIMENSIONS = (500, 500)

def main():
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
        self._display_surface.fill([255, 255, 255])
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.event.get()
        pygame.display.update()

    def on_render(self):
        red = (255, 0, 0)
        rect = pygame.Rect(100, 100, 100, 100)
        pygame.draw.rect(self._display_surface, red, rect)

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
