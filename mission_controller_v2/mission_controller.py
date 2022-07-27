
import numpy as np
import time
from threading import Thread


class MissionController:

    def __init__(self, robot):
        print("Creating MissionController!")
        # daemon thread is not good idea
        # I need the controller send the trajectory to the robot 
        # and this even if there is no set_trajectory from user in main thread
        # So, I want to finish the last trajectory points
        self.thread_poll_position = Thread(target=self._poll_position)

        self.thread_poll_position.start()

        self.robot = robot

        self.current_waypoint_idx = 0

    def set_trajectory(self, trajectory):
        self.current_waypoint_idx=0
        self.trajectory = trajectory
        

    def _poll_position(self):
        # thread switch to get trajectory from main thread
        
        def recurse_poll_position():
            
            time.sleep(1)
            # print(self.current_waypoint_idx)
            # print(self.trajectory)
            
            if self.current_waypoint_idx == len(self.trajectory):
                return
            position = self.robot.get_position()
            while np.all(position == self.trajectory[self.current_waypoint_idx]):
                self.current_waypoint_idx +=1
            # if not np.all(position == self.trajectory[self.current_waypoint_idx]):
                # self._send_navigation_command()
            self._send_navigation_command()
            self.current_waypoint_idx += 1
            recurse_poll_position()
        recurse_poll_position()

    def _send_navigation_command(self):

        print(f"Sending waypoint {self.current_waypoint_idx}")

        self.robot.set_navigation_command(self.trajectory[self.current_waypoint_idx])
