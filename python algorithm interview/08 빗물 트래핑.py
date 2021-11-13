from heapq import heapify
from os import stat_result


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 투 포인터를 최대로 이동
        # volume = 0
        # left = 0
        # right = len(height) - 1
        # left_max = height[left]
        # right_max = height[right]

        # while left < right:
        #     left_max = max(left_max, height[left])
        #     right_max = max(right_max, height[right])
        #     if left_max <= right_max:
        #         volume += left_max - height[left]
        #         left += 1
        #     else:
        #         volume += right_max - height[right]
        #         right -= 1

        # 스택 쌓기
        volume = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)

        return volume


sol = Solution()
print(sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(sol.trap(height=[4, 2, 0, 3, 2, 5]))
print(sol.trap(height=[2, 0, 2]))
