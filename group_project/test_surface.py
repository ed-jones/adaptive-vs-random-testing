import pygame
from pygame.locals import *
from group_project.colors import Colors
import random

DIMENSIONS = (500, 500)

class TestSurface:
    def __init__(self, title="Test Surface"):
        self._display_surface = pygame.Surface(DIMENSIONS)
        self._display_surface.fill(Colors.WHITE)

        pygame.font.init()
        font = pygame.font.SysFont("Calibri", 64)
        font_surface = font.render(title, True, Colors.BLACK)
        self._display_surface.blit(font_surface, (50, 50))

    def place_failure_area(self, randomCoords):
        rect = pygame.Rect(randomCoords[0], randomCoords[1], 10, 10)
        pygame.draw.rect(self._display_surface, Colors.RED, rect)

    def get_display_surface(self):
        return self._display_surface