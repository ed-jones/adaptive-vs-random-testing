from group_project.surfaces.test_surface import TestSurface
from group_project.globals.dimensions import *
import random

class ARTSurface(TestSurface):
    def __init__(self):
        self.title = "ART"
        self.position = (SURFACE_DIMENSIONS[0]+MARGIN*2, MARGIN)
        super().__init__()

    def generate_new_test_case(self) -> (int, int):
        random.seed()
        return (random.randint(0, SURFACE_DIMENSIONS[0]), random.randint(0, SURFACE_DIMENSIONS[1]))
