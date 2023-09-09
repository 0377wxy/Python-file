
"""
python解方程
"""

from scipy.optimize import fsolve


def solve_function(unsolved_value):
    x, y, z, k1, k2, k3 = unsolved_value[0], unsolved_value[1], unsolved_value[
        2], unsolved_value[3], unsolved_value[4], unsolved_value[5]
    return [
        (x + 0.013741629464285714*k1)**2 +
        (y - 0.05656328852872671*k2)**2 +
        (z + 0.9020389533190993*k3)**2-0.97936**2,

        (x - 0.9624402685072816*k1)**2 +
        (y - 0.057875549908980584*k2)**2 +
        (z - 0.2956590374696602*k3)**2-0.97936**2,

        (x - 0.008713666130514705*k1)**2 +
        (y + 0.9810599532781863*k2)**2 +
        (z - 0.008357029335171568*k3)**2-0.97936**2,

        (x + 1.015511607671801*k1)**2 +
        (y - 0.033140643513033176*k2)**2 +
        (z - 0.07795375444312796*k3)**2-0.97936**2,

        (x + 0.01633250956632653*k1)**2 +
        (y - 1.0160609654017858*k2)**2 +
        (z - 0.08625886878188775*k3)**2-0.97936**2,

        (x - 0.043886931046195655*k1)**2 +
        (y + 0.10544752038043478*k2)**2 +
        (z - 1.130653713060462*k3)**2-0.97936**2,
    ]

    # (x+0.97183090)**2+(y+0.01818483)**2+(z+0.0054202)**2-0.97936**2,
solved = fsolve(solve_function, [0, 0, 0, 0, 0, 0])
print(solved)


print("Program done!")

"""
运行结果：
[-1.  3.  5.]
Program done!

"""
