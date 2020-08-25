from group_project.surfaces.test_surface import TestSurface
from group_project.globals.dimensions import *
import random
import math

class ARTSurface(TestSurface):
    def __init__(self):
        self.title = "ART"
        self.position = (SURFACE_DIMENSIONS[0]+MARGIN*2, MARGIN)
        self.test_cases = []
        super().__init__()

    def place_test_case(self, coords):
        self.test_cases.append(coords)
        super().place_test_case(coords)

    def reset(self):
        super().reset()
        self.test_cases = []

    def generate_new_test_case(self) -> (int, int):
        k: int = 10
        max_distance = 0
        test_case: (int, int) = (0, 0)

        def calc_distance(a: (int, int), b: (int, int)):
            x1: int = a[0]
            y1: int = a[1]
            x2: int = b[0]
            y2: int = b[1]
            return math.sqrt(abs(x2-x1)+abs(y2-y1))

        for _i in range(k):
            random.seed()
            candidate = (random.randint(0, SURFACE_DIMENSIONS[0]), random.randint(0, SURFACE_DIMENSIONS[1]))
            min_distance = None
            for prev_test_case in self.test_cases:
                new_distance = calc_distance(prev_test_case, candidate)
                if min_distance == None or new_distance < min_distance:
                    min_distance = new_distance
            
            if min_distance > max_distance:
                test_case = candidate
                max_distance = min_distance

        return test_case
