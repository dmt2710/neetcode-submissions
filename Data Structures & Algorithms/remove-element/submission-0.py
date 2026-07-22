class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr_length = len(nums)
        track_index = 0
        count = 0
        for i in range(arr_length):
            if nums[i] != val:
                nums[track_index] = nums[i]
                track_index += 1  
                count += 1

        return count