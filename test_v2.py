
'''
Reviewed  by Muhammed El-Yamani
Date: 27/07/2022
'''
import time
import numpy as np
import argparse
from mission_controller_v2 import MissionController
from mission_controller_v2 import SimulatedRobot

'''
input data
I: initial point
T: trajectories
N: data points in each trajectory
N data points each in line x,y: line sperated space 
K: number actual data points for trajectory
K actual data points for trajectory x,y: line sperated space 
'''


class System:
    def __init__(self, display=True) -> None:
        self.initial_position = None
        self.trajectory = None
        self.actual_robot_trajectory = []
        self.calculated_robot_trajectory = []
        self.display = display

    def __get_initial_position(self):
        """
        I: initial point
        """
        l1 = list(map(float, input().strip().split(' ')))
        self.initial_position = np.array(l1)

    def __get_trajectory(self):
        """
        T: trajectories
        N: data points in each trajectory
        N data points each in line x,y: line sperated space
        """
        T = int(input().strip())
        for i in range(T):
            l2 = []
            N = int(input().strip())
            for j in range(N):
                l2.append(list(map(float, input().strip().split(' '))))
            trajectory = np.array(l2)
            yield trajectory

    def get_actual_robot_trajectory(self):
        '''
        K: number actual data points for trajectory
        K actual data points for trajectory x,y: line sperated space 
        '''
        l = []
        K = int(input().strip())
        for j in range(K):
            l.append(list(map(float, input().strip().split(' '))))
        self.actual_robot_trajectory = np.array(l)
        return self.actual_robot_trajectory

    def run_robot(self):
        self.__get_initial_position()
        if self.initial_position is None:
            raise Exception("Need Initial position")
        simulated_robot = SimulatedRobot(self.initial_position, self.display)
        controller = MissionController(simulated_robot, self.display)
        for self.trajectory in self.__get_trajectory():

            # set the trajectory comming from user input
            controller.set_trajectory(self.trajectory)
            # to switch to thread thread_poll_position
            time.sleep(1.01)
            # sleep main thread while thread_update terminated
            controller.sleep_till_move()
        # loop over the last trajectory
        while not controller.is_finish_trajectory():
            # to switch to thread thread_poll_position
            time.sleep(1.01)
            # sleep main thread while thread_update terminated
            controller.sleep_till_move()
        # the calculated path of the robot used in testing cases
        self.calculated_robot_trajectory = controller.get_calculated_robot_trajectory()


def test_normal_operation():
    ap = argparse.ArgumentParser(description="For validation purpose")
    ap.add_argument('--display', '-d', action='store_false')
    args = ap.parse_args()
    display = args.display
    sys = System(display)
    sys.run_robot()

    # load actual path of the robot used in testing cases
    actual_robot_trajectory = sys.get_actual_robot_trajectory()
    # the calculated path of the robot used in testing cases
    calculated_robot_trajectory = sys.calculated_robot_trajectory

    if np.all(actual_robot_trajectory.shape == calculated_robot_trajectory.shape) and np.all(actual_robot_trajectory == calculated_robot_trajectory):
        print("\n\nvalid test case\n\n")
    else:
        print("\n\nNot valid test case\n\n")

    print("Test complete")
    exit(0)


if __name__ == "__main__":
    test_normal_operation()
