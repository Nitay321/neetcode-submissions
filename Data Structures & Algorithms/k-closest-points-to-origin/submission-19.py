class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Sort the array in-place based on the squared distance
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        
        # Return the first k elements
        return points[:k]