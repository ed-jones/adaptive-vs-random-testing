import pygame
from pygame.locals import *
from group_project.globals.colors import Colors
from group_project.globals.dimensions import *

class TestSurface():
    def __init__(self):
        self._surface = pygame.Surface(SURFACE_DIMENSIONS)
        self._surface.fill(Colors.WHITE)

        pygame.font.init()
        font = pygame.font.SysFont("Calibri", round(SURFACE_DIMENSIONS[1]/10))
        font_surface = font.render(self.title, True, Colors.BLACK)
        self._surface.blit(font_surface, (10, 10))

    def place_failure_area(self, coords, failure_rate):
        self.failure_area = {
            "x": coords[0], 
            "y": coords[1], 
            "width": failure_rate*SURFACE_DIMENSIONS[0], 
            "height": failure_rate*SURFACE_DIMENSIONS[1]
        }
        rect = pygame.Rect(
            self.failure_area["x"],
            self.failure_area["y"],
            self.failure_area["width"],
            self.failure_area["height"],
        )
        pygame.draw.rect(self._surface, Colors.RED, rect)

    def place_test_case(self, coords):
        self.test_case = coords
        pygame.draw.circle(self._surface, Colors.BLUE, coords, 5)

    def check_failure(self) -> bool:
        if self.test_case[0] > self.failure_area["x"]\
            and self.test_case[0] < self.failure_area["x"] + self.failure_area["width"]\
            and self.test_case[1] > self.failure_area["y"]\
            and self.test_case[1] <  self.failure_area["y"] + self.failure_area["height"]:
            return True
        else:
            return False

    def draw(self, surface):
        surface.blit(self._surface, self.position)