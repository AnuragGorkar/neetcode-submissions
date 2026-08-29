class CountSquares:

    def __init__(self):
        self.points_dict = defaultdict(int)
        self.x_dict = defaultdict(set)
        self.y_dict = defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points_dict[str(point[0])+"-"+str(point[1])] += 1
        self.x_dict[point[0]].add(point[1])
        self.y_dict[point[1]].add(point[0])

    def count(self, point: List[int]) -> int:
        x_points = self.x_dict[point[0]]
        y_points = self.y_dict[point[1]]
        count = 0

        for x_point in x_points:
            dis = abs(point[1]-x_point)
            if dis>0:
                if (point[0]-dis) in y_points and str(point[0]-dis)+"-"+str(x_point) in self.points_dict:
                    count += (self.points_dict[str(point[0])+"-"+str(x_point)] * self.points_dict[str(point[0]-dis)+"-"+str(point[1])] * self.points_dict[str(point[0]-dis)+"-"+str(x_point)])
                if (point[0]+dis) in y_points and str(point[0]+dis)+"-"+str(x_point) in self.points_dict:
                    count += (self.points_dict[str(point[0])+"-"+str(x_point)] * self.points_dict[str(point[0]+dis)+"-"+str(point[1])] * self.points_dict[str(point[0]+dis)+"-"+str(x_point)])

        return count
