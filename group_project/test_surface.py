import pygame
from pygame.locals import *
from group_project.colors import Colors
from group_project.globals import *
import random

class TestSurface:
    def __init__(self, title="Test Surface"):
        self._display_surface = pygame.Surface(SURFACE_DIMENSIONS)
        self._display_surface.fill(Colors.WHITE)

        pygame.font.init()
        font = pygame.font.SysFont("Calibri", round(SURFACE_DIMENSIONS[1]/10))
        font_surface = font.render(title, True, Colors.BLACK)
        self._display_surface.blit(font_surface, (10, 10))

    def place_failure_area(self, randomCoords, failure_rate):
        rect = pygame.Rect(
            randomCoords[0], 
            randomCoords[1], 
            failure_rate*SURFACE_DIMENSIONS[0], 
            failure_rate*SURFACE_DIMENSIONS[1]
        )
        pygame.draw.rect(self._display_surface, Colors.RED, rect)

    def place_test_case(self, randomCoords):
        pygame.draw.circle(self._display_surface, Colors.BLUE, randomCoords, 5)

    def get_display_surface(self):
        return self._display_surface