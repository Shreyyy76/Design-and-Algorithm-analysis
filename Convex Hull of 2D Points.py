def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
def is_valid_edge(points, p, q):
    positive = negative = 0
    for r in points:
        if r != p and r != q:
            orient = orientation(p, q, r)
            if orient > 0:
                positive += 1
            elif orient < 0:
                negative += 1
        if positive and negative:
            return False
    return True
def convex_hull_brute_force(points):
    hull = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if is_valid_edge(points, points[i], points[j]):
                hull.append(points[i])
                hull.append(points[j])
    hull = list(set(hull))
    hull.sort(key=lambda p: (p[0], p[1]))
    return hull
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
convex_hull = convex_hull_brute_force(points)
print("Convex Hull:", convex_hull)
