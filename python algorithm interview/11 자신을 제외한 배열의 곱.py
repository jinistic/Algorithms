class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_from_left = [1]
        product_from_right = [1]
        pl = 1
        pr = 1
        for i in range(len(nums) - 1):
            pl *= nums[i]
            pr *= nums[-i - 1]
            product_from_left.append(pl)
            product_from_right.append(pr)

        return [
            product_from_left[i] * product_from_right[-i - 1] for i in range(len(nums))
        ]


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
print(sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
