class Solution:
    def minTimeToVisitAllPoints(points):
        res = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            res += max(abs(x2 - x1), abs(y2 - y1))

            x1, y1 = x2, y2
        return res


# Explanation

# We start with the last point and reduce the number of points by one.
# Then get the second point and see the difference between the change in x and change in y.
# Whichever is greater, is the min time to visit that point. Repeat this and sum the time to
# get the final answer.
