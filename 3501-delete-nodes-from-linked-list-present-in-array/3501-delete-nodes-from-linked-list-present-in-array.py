# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head        
        current = dummy        
        while current.next:
            if current.next.val in remove_set:
                current.next = current.next.next
            else:
                current = current.next        
        return dummy.next
        