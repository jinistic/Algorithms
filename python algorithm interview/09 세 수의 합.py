class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return results


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(sol.threeSum(nums=[]))
print(sol.threeSum(nums=[0]))
print(sol.threeSum(nums=[1, -1, -1, 0]))
