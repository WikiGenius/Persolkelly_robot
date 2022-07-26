
'''
Reviewed  by Muhammed El-Yamani
Date: 27/07/2022
'''
import time
from threading import Thread

import random


class SimulatedRobot:

    def __init__(self, initial_position, display=True):
        self.display = display
        if self.display:
            print("Creating SimulatedRobot!")

        self.position = initial_position
        
    def get_position(self):
        return self.position

    def sleep_till_move(self):
        if (self.thread_update.isAlive()):
            time.sleep(2)

    def set_navigation_command(self, waypoint):
        if self.display:
            print(f"Commanding robot to move to {waypoint}")

        def update():
            # depends on speed of the robot
            time.sleep(random.uniform(1.0, 2.0))
            if self.display:
                print(f"Robot is now at {waypoint}")

            self.position = waypoint
        self.thread_update = Thread(target=update)
        self.thread_update.start()

        self.sleep_till_move()
