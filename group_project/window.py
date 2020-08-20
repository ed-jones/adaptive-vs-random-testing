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
        self.test_count = 1
        self.paused = False
 
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("CSCI318 Group Project")
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SCALED)
        self._display_surface.fill(Colors.BLACK)
        self._running = True

        # Create test surfaces
        self.rt_surface = RTSurface()
        self.art_surface = ARTSurface()

        # Generate initial failure area
        max_x = SURFACE_DIMENSIONS[0]-self.failure_rate*SURFACE_DIMENSIONS[0]
        max_y = SURFACE_DIMENSIONS[1]-self.failure_rate*SURFACE_DIMENSIONS[1]
        failure_area_coords = self.generate_random_coords((max_x, max_y))

        # Add failure area to test surfaces
        self.rt_surface.place_failure_area(failure_area_coords, self.failure_rate)
        self.art_surface.place_failure_area(failure_area_coords, self.failure_rate)

        # Add initial test case (same on both)
        test_case_coords = self.generate_random_coords()
        self.rt_surface.place_test_case(test_case_coords)
        self.art_surface.place_test_case(test_case_coords)
        self.print_test_result()

    def generate_random_coords(self, max_coords: (int, int) = SURFACE_DIMENSIONS) -> (int, int):
        random.seed()
        return (random.randint(0, max_coords[0]), random.randint(0, max_coords[1]))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.event.get()
        pygame.display.update()

        # Generate and place a new test case
        if not (self.rt_surface.check_failure() or self.art_surface.check_failure()):
            self.rt_surface.place_test_case(self.rt_surface.generate_new_test_case())
            self.art_surface.place_test_case(self.rt_surface.generate_new_test_case())
            self.test_count += 1 
            self.print_test_result()

        # Draw test surfaces to window
        self._display_surface.blit(self.rt_surface.get_display_surface(), (MARGIN, MARGIN))
        self._display_surface.blit(self.art_surface.get_display_surface(), (SURFACE_DIMENSIONS[0]+MARGIN*2, MARGIN))

        pygame.time.wait(100)

    def print_test_result(self):
        print("Test case " + str(self.test_count) + ":", 
            "RT -",
            "HIT!!" if self.rt_surface.check_failure() else "missed",
            "    ",
            "ART -",
            "HIT!!" if self.art_surface.check_failure() else "missed",
        )

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            if not self.paused:
                self.on_loop()
            
        self.on_cleanup()
