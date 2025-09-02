class Solution(object):
    def majorityElement(self, nums):
        votes = 0
        majority = None
    
        for num in nums:
            if votes == 0:
                majority = num
            votes += (1 if num == majority else -1)
        return majority

