import pygame
from group_project.rt_surface import RTSurface 
from group_project.art_surface import ARTSurface
from group_project.globals import *
import random

class Competition:
    def __init__(self):
        self.test_count = 1
        self.competition_number = 0
        self.max_competitions = 1
        self.rt_wins = 0
        self.art_wins = 0

        self.failure_rate: float = 0
        try:
            failure_rate_string: str = input("Enter a failure rate: ")
            self.failure_rate = round(float(failure_rate_string), 2)
            assert self.failure_rate > 0 and self.failure_rate < 1
        except ValueError:
            if failure_rate_string == '':
                print("No failure rate supplied, using 0.01 as default")
                self.failure_rate = 0.01
            else:
                print("Failure rate must be a floating point number.")
                exit()
        except AssertionError:
            print("Failure rate must lie between 0 and 1 exclusively.")
            exit()

        self.on_init()

    def on_init(self):
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

    def place_test_cases(self):
        if self.is_finished():
            self.reset()
        else:
            self.rt_surface.place_test_case(self.rt_surface.generate_new_test_case())
            self.art_surface.place_test_case(self.rt_surface.generate_new_test_case())
            self.test_count += 1 
            self.print_test_result()

    def is_finished(self) -> bool:
        return self.rt_surface.check_failure() or self.art_surface.check_failure()

    def draw_surfaces(self, display_surface):
        # Draw test surfaces to window
        display_surface.blit(self.rt_surface.get_display_surface(), (MARGIN, MARGIN))
        display_surface.blit(self.art_surface.get_display_surface(), (SURFACE_DIMENSIONS[0]+MARGIN*2, MARGIN))

    def print_test_result(self):
        print("Test case " + str(self.test_count) + ":", 
            "RT -",
            "HIT!! " if self.rt_surface.check_failure() else "missed",
            "    ",
            "ART -",
            "HIT!! " if self.art_surface.check_failure() else "missed",
        )

    def reset(self):
        if self.rt_surface.check_failure():
            self.rt_wins += 1
        elif self.art_surface.check_failure():
            self.art_wins += 1

        if self.competition_number == 0:
            max_competitions_string = input("How many more competitions do you want to run? ")
            self.max_competitions: int = int(max_competitions_string)
        if self.competition_number < self.max_competitions:
            self.competition_number += 1
            self.on_init()
        else:
            print(self.competition_number, "competitions have been completed, of which RT wins", 
                self.rt_wins, "times and ART wins", self.art_wins, "times.")
            exit()
