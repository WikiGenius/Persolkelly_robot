
import time
import numpy as np

from mission_controller_v2.mission_controller import MissionController
from mission_controller_v2.simulated_robot import SimulatedRobot


def test_normal_operation():

    simulated_robot = SimulatedRobot(np.array([0.0, 0.0]))
    controller = MissionController(simulated_robot)

    # set the first trajectory

    controller.set_trajectory(np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]]))

    time.sleep(2.5)

    # # now set a different trajectory before the first trajectory completes
    # print("X")
    controller.set_trajectory(np.array([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0]]))

    time.sleep(2.5)
    thread_poll_position = controller.thread_poll_position
    thread_poll_position.join()
    print("Test complete")

    exit(0)


if __name__ == "__main__":
    test_normal_operation()
