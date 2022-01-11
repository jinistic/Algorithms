# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        root = start = None  # None
        root.next = head

        # start, end 이동
        for _ in range(left - 1):
            start = start.next
        end = start.next  # end = 3

        # 반복하면서 뒤집기
        for _ in range(right - left):
            tmp = start.next  # tmp = 3
            start.next = end.next  # 2 -> 4 , tmp = 3
            end.next = end.next.next  # 3 -> 5
            start.next.next = tmp  # 4 -> 3

        return root.next


"""
           left = 3,     right = 6

root -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8  
           start end
                 tmp

root -> 1 -> 2 -> 4 -> 3 -> 5 -> 6 -> 7 -> 8  
           start      end      
                      tmp

root -> 1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7 -> 8  
           start      tmp  end


root -> 1 -> 2 -> 6 -> 5 -> 4 -> 3 -> 7 -> 8  
           start      tmp       end
"""

