import math
def euclidean_distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)
def k_closest_points(points, k):
    points.sort(key=euclidean_distance)
    return points[:k]
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
result = k_closest_points(points, k)
print("The k closest points to the origin are:", result)
