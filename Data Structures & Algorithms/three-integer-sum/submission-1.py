class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        print(nums)
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and num == nums[i-1]:
                continue

            while l < r:
                current_sum = num + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]]) #[-1,-1,2]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    l += 1
                    r -= 1

        return res