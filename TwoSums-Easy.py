class Solution(object):
    def twoSum(self, nums, target):
        pre_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pre_map:
                return [pre_map[diff], i]
            pre_map[n] = i
        return
