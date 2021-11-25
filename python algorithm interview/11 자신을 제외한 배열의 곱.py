class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_from_left = []
        product_from_right = []
        pl = 1
        pr = 1
        for i in range(len(nums)):
            product_from_left.append(pl)
            product_from_right.append(pr)
            pl *= nums[i]
            pr *= nums[-i - 1]

        return [
            product_from_left[i] * product_from_right[-i - 1] for i in range(len(nums))
        ]


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
print(sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
