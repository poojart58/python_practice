## Two Sum Leetcode Question
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        for i in range(len(nums)):
            if nums[i] in diction:
                return [diction[nums[i]], i]
            else:
                diction[target - nums[i]] = i
