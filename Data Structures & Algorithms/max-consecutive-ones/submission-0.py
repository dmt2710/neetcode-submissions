class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tracked = 0
        max_tracked = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tracked += 1
                max_tracked = max(max_tracked, tracked)
            else:
                tracked = 0
        
        return max_tracked