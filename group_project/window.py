import pygame
from pygame.locals import *
from group_project.colors import Colors
from group_project.rt_surface import RTSurface 
from group_project.art_surface import ARTSurface
from group_project.globals import *
import random

class Window:
    def __init__(self, failure_rate):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = (SURFACE_DIMENSIONS[0]*2+MARGIN*3, SURFACE_DIMENSIONS[1]+MARGIN*2)
        self.failure_rate = failure_rate
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surface.fill(Colors.BLACK)
        self._running = True

        rt_surface = RTSurface()
        art_surface = ARTSurface()

        random.seed()
        max_x = SURFACE_DIMENSIONS[0]-self.failure_rate*SURFACE_DIMENSIONS[0]
        max_y = SURFACE_DIMENSIONS[1]-self.failure_rate*SURFACE_DIMENSIONS[1]
        randomCoords = (random.randint(0, max_x), random.randint(0, max_y))

        rt_surface.place_failure_area(randomCoords, self.failure_rate)
        art_surface.place_failure_area(randomCoords, self.failure_rate)

        self._display_surface.blit(rt_surface.get_display_surface(), (MARGIN, MARGIN))
        self._display_surface.blit(art_surface.get_display_surface(), (SURFACE_DIMENSIONS[0]+MARGIN*2, MARGIN))

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
