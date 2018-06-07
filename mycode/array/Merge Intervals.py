#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda x: x.start)
        N = len(intervals)
        i = 0
        ret_interval = []
        while i < N:
            s = intervals[i].start
            e = intervals[i].end
            j = i + 1
            while j < N and intervals[j].start <= e:
                e = max(e, intervals[j].end)
                j += 1
            ret_interval.append(Interval(s, e))
            i = j
        return ret_interval