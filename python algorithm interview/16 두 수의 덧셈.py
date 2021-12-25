# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def get_number(head: Optional[ListNode]):
            node = head
            node_list = []
            while node:
                node_list.append(str(node.val))
                node = node.next

            return int("".join(node_list[::-1]))

        result = get_number(l1) + get_number(l2)
        result = list(map(int, str(result)))

        prev = None
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node

        return node


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
