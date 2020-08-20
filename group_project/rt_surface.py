from group_project.test_surface import TestSurface
from group_project.globals import *
import random

class RTSurface(TestSurface):
    def __init__(self):
        super().__init__("RT")

    def generate_new_test_case(self) -> (int, int):
        random.seed()
        return (random.randint(0, SURFACE_DIMENSIONS[0]), random.randint(0, SURFACE_DIMENSIONS[1]))