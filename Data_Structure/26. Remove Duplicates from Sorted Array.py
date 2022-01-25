class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
