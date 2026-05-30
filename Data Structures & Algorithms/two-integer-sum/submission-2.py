class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            remain = target - num

            if remain in dic:
                return [dic[remain], i]

            dic[num] = i

