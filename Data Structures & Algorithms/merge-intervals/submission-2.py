class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_interval = sorted(intervals, key=lambda a:a[0])

        res = []

        cur_l, cur_r = sort_interval[0]

        for i in range(1,len(intervals)):
            l, r = sort_interval[i]

            if l<=cur_r:
                cur_r = max(cur_r,r)
            else:
                res.append([cur_l, cur_r])
                cur_l, cur_r = l,r
        res.append([cur_l,cur_r])

        return res