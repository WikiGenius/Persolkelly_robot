
import numpy as np

import time
import threading
from threading import Thread

import random


class SimulatedRobot:

    def __init__(self, initial_position):
        print("Creating SimulatedRobot!")

        self.position = initial_position
    def get_position(self):
        return self.position

    
    def set_navigation_command(self, waypoint):

        print(f"Commanding robot to move to {waypoint}")

        def update():
            # depends on speed of the robot
            time.sleep(random.uniform(1.0, 2.0))

            print(f"Robot is now at {waypoint}")

            self.position = waypoint
        thread_update = Thread(target=update)
        thread_update.start()
        # thread_update.join()
        time.sleep(2)