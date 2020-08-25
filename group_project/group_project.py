import pygame
from group_project.surfaces.rt_surface import RTSurface 
from group_project.surfaces.art_surface import ARTSurface
from group_project.globals.dimensions import *
from group_project.game import Game
import random
import math

class GroupProject(Game):
    def __init__(self, failure_rate):
        super().__init__()

        self.test_count = 0
        self.competition_number = 0
        self.max_competitions = 1
        self.rt_wins = 0
        self.art_wins = 0
        self.failure_rate: float = failure_rate
        self.rt_surface = RTSurface()
        self.art_surface = ARTSurface()

    def on_init(self):
        super().on_init()
        self.build_test_surfaces()

    def build_test_surfaces(self):
        def generate_random_coords(max_coords: (int, int) = SURFACE_DIMENSIONS) -> (int, int):
            random.seed()
            return (random.randint(0, max_coords[0]), random.randint(0, max_coords[1]))

        # Reset test surfaces
        self.rt_surface.reset()
        self.art_surface.reset()
        
        # Generate initial failure area
        square_dimension = math.sqrt(self.failure_rate*SURFACE_DIMENSIONS[0]*SURFACE_DIMENSIONS[1])
        max_x = round(SURFACE_DIMENSIONS[0] - square_dimension)
        max_y = round(SURFACE_DIMENSIONS[1] - square_dimension)
        failure_area_coords = generate_random_coords((max_x, max_y))

        # Add failure area to test surfaces
        self.rt_surface.place_failure_area(failure_area_coords, square_dimension)
        self.art_surface.place_failure_area(failure_area_coords, square_dimension)

        # Add initial test case (same on both)
        random_coords = generate_random_coords()
        self.place_test_cases(random_coords, random_coords)


    def on_loop(self):
        self.place_test_cases(\
            self.rt_surface.generate_new_test_case(),\
            self.art_surface.generate_new_test_case()\
        )

    def check_failure(self):
        if self.rt_surface.check_failure() or self.art_surface.check_failure():
            self.reset()

    def place_test_cases(self, rt_coords, art_coords):
        self.rt_surface.place_test_case(rt_coords)
        self.art_surface.place_test_case(art_coords)

        self.test_count += 1 

        print("Test case " + str(self.test_count) + ":", 
            "RT -",
            "HIT!! " if self.rt_surface.check_failure() else "missed",
            "    ",
            "ART -",
            "HIT!! " if self.art_surface.check_failure() else "missed",
        )

        self.rt_surface.draw(self._display_surface)
        self.art_surface.draw(self._display_surface)
        pygame.display.update()

        self.check_failure()

    def reset(self):
        print()
        
        if self.rt_surface.check_failure():
            self.rt_wins += 1
        if self.art_surface.check_failure():
            self.art_wins += 1

        if self.competition_number == 0:
            max_competitions_string = input("How many more competitions do you want to run? ")
            try:
                self.max_competitions: int = int(max_competitions_string)
            except ValueError:
                self.max_competitions = 0

        if self.competition_number < self.max_competitions:
            self.competition_number += 1
            self.test_count = 0
            self.build_test_surfaces()
        else:
            print(self.competition_number + 1, "competitions have been completed, of which RT wins", 
                self.rt_wins, "times and ART wins", self.art_wins, "times.")
            exit(0)
