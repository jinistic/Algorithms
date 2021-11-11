class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute-Force, O(n^2)
        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # O(n^2), but "in" operator -> faster
        # for i in range(0, len(nums) - 1):
        #     if target - nums[i] in nums[i + 1 :]:
        #         return [i, i + 1 + nums[i + 1 :].index(target - nums[i])]

        # O(n)
        # nums_dict = {}
        # for i, num in enumerate(nums):
        #     nums_dict[num] = i
        #
        # for i, num in enumerate(nums):
        #     if target - num in nums_dict and i != nums_dict[target - num]:
        #         return [i, nums_dict[target - num]]

        # O(n), simpler version
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            else:
                nums_dict[num] = i


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
