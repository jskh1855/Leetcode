class Solution:

    def get_slope(self, p1, p2):

        return (p2[1]-p1[1])/(p2[0]-p1[0]) if p2[0]-p1[0] != 0 else float('inf')

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        standard_slope = self.get_slope(coordinates[0], coordinates[1])
        answer = True

        for coordinate in coordinates[2:]:

            if self.get_slope(coordinates[0], coordinate) != standard_slope:

                answer = False
                break

        return answer
