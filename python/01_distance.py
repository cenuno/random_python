import numpy as np
from scipy.spatial.distance import pdist

X = [[0, 1, 2],
    [3, 4, 5]]

euclidean_distance = np.round(pdist(X, "euclidean"), 3)
manhattan_distance = np.round(pdist(X, "cityblock"), 3)

print(f"Euclidean distance of {X} is {euclidean_distance}")
print(f"Manhattan distance of {X} is {manhattan_distance}")

note = """
The Minkowski distance defines a distance between two points in a normed vector space.

Special cases:

\t* When p=1, the distance is known as the Manhattan distance.
\t* When p=2, the distance is known as the Euclidean distance.
\t* In the limit that p --> +infinity, the distance is known as the Chebyshev distance.

See https://www.npmjs.com/package/compute-minkowski-distance for more information.
"""

print(note)

minkowski_distance = np.round(pdist(X, 'minkowski', p=1), 3)

print(f"When p=1, the Minkowski distance ({minkowski_distance}) of {X} is equal to the Manhattan distance ({manhattan_distance})")

minkowski_distance = np.round(pdist(X, 'minkowski', p=2), 3)

print(f"When p=2, the Minkowski distance ({minkowski_distance}) of {X} is equal to the Euclidean distance ({euclidean_distance})")

minkowski_distance = np.round(pdist(X, 'minkowski', p=3), 3)

print(f"When p>2, the Minkowski distance ({minkowski_distance}) of {X} will be smaller than either the Manhattan or Euclidean distance.")
