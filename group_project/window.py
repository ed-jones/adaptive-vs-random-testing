import pygame
from pygame.locals import *
from group_project.colors import Colors
from group_project.rt_surface import RTSurface 
from group_project.art_surface import ARTSurface
import random

DIMENSIONS = (1018, 512)

class Window:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = DIMENSIONS
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surface.fill(Colors.BLACK)
        self._running = True

        rt_surface = RTSurface()
        art_surface = ARTSurface()

        random.seed()
        randomCoords = (random.randint(0, 500), random.randint(0, 500))

        rt_surface.place_failure_area(randomCoords)
        art_surface.place_failure_area(randomCoords)

        self._display_surface.blit(rt_surface.get_display_surface(), (6, 6))
        self._display_surface.blit(art_surface.get_display_surface(), (512, 6))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.event.get()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            
        self.on_cleanup()
