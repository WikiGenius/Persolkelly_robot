
import time
import numpy as np

from mission_controller_v2.mission_controller import MissionController
from mission_controller_v2.simulated_robot import SimulatedRobot

'''
input data
I: initial point
T: trajectories
N: data points in each trajectory
N data points each in line x,y: line sperated space 
''' 

class System:
    def __init__(self) -> None:
        self.initial_position = None
        self.trajectory = None

    def __get_initial_position(self):
        l1=list(map(float, input().strip().split(' ')))
        self.initial_position = np.array(l1)

    def __get_input_data(self):
        
        T= int(input().strip())
        for i in range(T):
            l2 = []
            N= int(input().strip())
            for j in range(N):
                l2.append(list(map(float, input().strip().split(' '))))
            trajectory = np.array(l2)
            yield trajectory

    def run_robot(self):
        self.__get_initial_position()
        if self.initial_position is None:
            raise Exception("Need Initial position")
        simulated_robot = SimulatedRobot(self.initial_position)
        controller = MissionController(simulated_robot)

        for self.trajectory in self.__get_input_data():

            # set the trajectory comming from user input

            controller.set_trajectory(self.trajectory)

            time.sleep(2.5)

        thread_poll_position = controller.thread_poll_position
        thread_poll_position.join()

def test_normal_operation():
    System().run_robot()
    print("Test complete")
    exit(0)


if __name__ == "__main__":
    test_normal_operation()
