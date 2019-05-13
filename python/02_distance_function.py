import numpy as np


def calculate_distance(a, b, c=2, verbose=True):
    """
    Calculates the distance of two arrays. Returns a float.
    """
    if verbose and c==1:
        print("Calculating the Manhattan distance:")
    elif verbose and c==2:
        print("Calculating the Euclidean distance:")

    elif verbose and c>2:
        print("Calculating the Minkowski distance:")
    else:
        pass

    diff_ab = a - b
    abs_ab = np.absolute(diff_ab)
    power_ab = abs_ab**c
    sum_ab = power_ab.sum()
    root_ab = np.power(sum_ab, 1/c)
    output = np.round(root_ab, 3)

    return output



i = np.array([1, 2])
j = np.array([4, 6])

for num in [1, 2, 3]:
    output = calculate_distance(a=i, b=j, c=num)
    print(output)
