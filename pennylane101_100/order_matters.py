#!/usr/bin/env python3

import sys

import pennylane as qml
from pennylane import numpy as np


def compare_circuits(angles):
    """Given two angles, compare two circuit outputs that have their order of operations flipped: RX then RY VERSUS RY then RX.

    Args:
        - angles (np.ndarray): Two angles

    Returns:
        - (float): | < \sigma^x >_1 - < \sigma^x >_2 |
    """

    # QHACK #
    device = qml.device("default.qubit", wires=1)

    theta1, theta2 = angles

    @qml.qnode(device)
    def XY_rotation(t1, t2):
        qml.RX(t1, wires=0)
        qml.RY(t2, wires=0)
        return qml.expval(qml.PauliX(0))

    @qml.qnode(device)
    def YX_rotation(t1, t2):
        qml.RY(t1, wires=0)
        qml.RX(t2, wires=0)
        return qml.expval(qml.PauliX(0))

    return abs(XY_rotation(theta1, theta2) - YX_rotation(theta2, theta1))

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    angles = np.array(sys.stdin.read().split(","), dtype=float)
    output = compare_circuits(angles)
    print(f"{output:.6f}")
