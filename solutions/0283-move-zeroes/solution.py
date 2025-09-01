class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[i], nums[r] = nums[r], nums[i]
                i += 1
       



