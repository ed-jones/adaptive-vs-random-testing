import pygame
from pygame.locals import *
from group_project.globals.colors import Colors
from group_project.globals.dimensions import *

class TestSurface:
    def __init__(self, title="Test Surface"):
        self._display_surface = pygame.Surface(SURFACE_DIMENSIONS)
        self._display_surface.fill(Colors.WHITE)

        pygame.font.init()
        font = pygame.font.SysFont("Calibri", round(SURFACE_DIMENSIONS[1]/10))
        font_surface = font.render(title, True, Colors.BLACK)
        self._display_surface.blit(font_surface, (10, 10))

    def place_failure_area(self, randomCoords, failure_rate):
        self.failure_area = {
            "x": randomCoords[0], 
            "y": randomCoords[1], 
            "width": failure_rate*SURFACE_DIMENSIONS[0], 
            "height": failure_rate*SURFACE_DIMENSIONS[1]
        }
        rect = pygame.Rect(
            self.failure_area["x"],
            self.failure_area["y"],
            self.failure_area["width"],
            self.failure_area["height"],
        )
        pygame.draw.rect(self._display_surface, Colors.RED, rect)

    def place_test_case(self, randomCoords):
        self.test_case = randomCoords
        pygame.draw.circle(self._display_surface, Colors.BLUE, randomCoords, 5)

    def check_failure(self) -> bool:
        if self.test_case[0] > self.failure_area["x"]\
            and self.test_case[0] < self.failure_area["x"] + self.failure_area["width"]\
            and self.test_case[1] > self.failure_area["y"]\
            and self.test_case[1] <  self.failure_area["y"] + self.failure_area["height"]:
            return True
        else:
            return False

    def get_display_surface(self):
        return self._display_surface