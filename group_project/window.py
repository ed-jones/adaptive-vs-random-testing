import pygame
from pygame.locals import *
from group_project.globals.colors import Colors
from group_project.globals.dimensions import *
from group_project.competition import Competition

class Window:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.width, self.height \
            = (SURFACE_DIMENSIONS[0]*2+MARGIN*3, SURFACE_DIMENSIONS[1]+MARGIN*2)
        self.paused = False
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self.display_surface = pygame.display.set_mode(self.size, 
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SCALED)
        self.display_surface.fill(Colors.BLACK)
        self.running = True

        self.competition = Competition()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.event.get()
        pygame.display.update()

        self.competition.place_test_cases()
        self.competition.draw_surfaces(self.display_surface)

        pygame.time.wait(100)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            if not self.paused:
                self.on_loop()
            
        self.on_cleanup()
