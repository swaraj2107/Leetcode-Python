class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        n = len(intervals)
        result = [intervals[0]]
        dif = 0

        for i in range(1,n):
            if((intervals[i][0]) > (result[i-dif-1][1])):
                result.append(intervals[i])

            else:
                result[i-dif-1][1] = max(result[i-dif-1][1],intervals[i][1])
                dif += 1

        return result
