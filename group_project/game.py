# http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *
from group_project.globals.dimensions import *
from group_project.globals.colors import Colors

class Game:
    def __init__(self):
        self._running = True
        self.size = self.width, self.height \
            = (SURFACE_DIMENSIONS[0]*2+MARGIN*3, SURFACE_DIMENSIONS[1]+MARGIN*2)
        self._display_surface = pygame.display.set_mode(self.size, 
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SCALED)
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self._display_surface.fill(Colors.BLACK)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            pygame.display.update()
            # pygame.time.wait(100)
        self.on_cleanup()