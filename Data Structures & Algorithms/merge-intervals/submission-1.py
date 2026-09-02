class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1, 2, 3, 4, 5, 6, 7
        # -     - 
        # -           -  
        #                -  -

        intervals.sort()
        output = [] # [[1, 4]]

        for interval in intervals: # [2, 3]

            if not output or interval[0] > output[-1][1]: # 2 < 4
                output.append(interval)

            else: 
                output[-1][1] = max(output[-1][1], interval[1]) # 3

        return output