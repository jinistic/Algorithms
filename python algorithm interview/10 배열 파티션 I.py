class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


sol = Solution()
print(sol.arrayPairSum(nums=[1, 4, 3, 2]))
print(sol.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
