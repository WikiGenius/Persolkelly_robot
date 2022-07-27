
import numpy as np
import time
from threading import Thread
import threading

class MissionController:

    def __init__(self, robot):
        print("Creating MissionController!")
        
        self.thread_poll_position = Thread(target=self._poll_position, daemon=True)

        self.thread_poll_position.start()

        self.robot = robot

        self.current_waypoint_idx = 0
        self.calculated_robot_trajectory=[]
        self.calculated_robot_trajectory.append(self.robot.get_position())
        self.empty_trajectory = False
        self.is_robotMove = False
        
    def set_trajectory(self, trajectory):
        self.current_waypoint_idx=0
        self.trajectory = trajectory
        
    def get_calculated_robot_trajectory(self):
        return np.array(self.calculated_robot_trajectory)
    def is_finish_trajectory(self):
        return self.empty_trajectory
    def is_robot_move(self):
        return self.is_robotMove

    def _poll_position(self):
        # thread switch to get trajectory from main thread
        
        def recurse_poll_position():
            
            time.sleep(1)
            self.is_robotMove = False
            self.empty_trajectory = False
            if self.current_waypoint_idx == len(self.trajectory):
                self.empty_trajectory = True
                recurse_poll_position()
            position = self.robot.get_position()
            while np.all(position == self.trajectory[self.current_waypoint_idx]):
                self.current_waypoint_idx +=1
                if self.current_waypoint_idx == len(self.trajectory):
                    self.empty_trajectory = True
                    recurse_poll_position()
            self.is_robotMove = True
            self._send_navigation_command()
            self.current_waypoint_idx += 1
            
            recurse_poll_position()
        recurse_poll_position()

    def _send_navigation_command(self):

        print(f"Sending waypoint {self.current_waypoint_idx}")
        self.calculated_robot_trajectory.append(self.trajectory[self.current_waypoint_idx])
        self.robot.set_navigation_command(self.trajectory[self.current_waypoint_idx])