
def distance(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

class ConvexHull(object):  
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        
        difference = (
            ((p2[0] - origin[0]) * (p1[1] - origin[1]))
            - ((p1[0] - origin[0]) * (p2[1] - origin[1]))
        )

        return difference

    def compute_hull(self):
       
        points = self._points

        start = points[0]
        min_x = start[0]
        for p in points[1:]:
            if p[0] < min_x:
                min_x = p[0]
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

  
ch = ConvexHull()
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    ch.add([x,y])

mat = ch.get_hull_points()
print(mat)

l = len(mat)-1

