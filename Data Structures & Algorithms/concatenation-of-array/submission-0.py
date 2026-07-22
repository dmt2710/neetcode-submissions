class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newArr = [0] * (2 * length)

        for i in range(len(nums)):
            newArr[i] = nums[i]
            newArr[i+length] = nums[i]

        return newArr