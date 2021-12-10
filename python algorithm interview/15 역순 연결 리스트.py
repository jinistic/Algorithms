# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 반복
        # node = head
        # prev = None

        # while node:
        #     next = node.next
        #     node.next = prev
        #     prev = node
        #     node = next

        # return prev

        # 재귀
        def reverse(
            node: Optional[ListNode], prev: Optional[ListNode] = None
        ) -> Optional[ListNode]:
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
