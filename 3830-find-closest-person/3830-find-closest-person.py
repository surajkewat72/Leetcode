class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)  # distance of Person 1 from Person 3
        dist2 = abs(y - z)  # distance of Person 2 from Person 3

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
        