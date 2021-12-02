# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

        # node = head
        # q = []

        # while node is not None:
        #     q.append(node.val)
        #     node = node.next

        # for i in range(len(q) // 2):
        #     if q[i] != q[-i - 1]:
        #         return False

        # return True


# sol = Solution()
# print(sol.isPalindrome(head=ListNode([1, 2, 2, 1])))
# print(sol.isPalindrome(head=ListNode([1, 2])))

