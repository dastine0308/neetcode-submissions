class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        num_unique = set(nums)
        return len(nums) != len(num_unique)