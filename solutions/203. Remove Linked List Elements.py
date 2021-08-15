# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        current_node = head
        while current_node and current_node.next:
            if current_node.next.val == val:
                if current_node.next.next:
                    current_node.next = current_node.next.next
                else:
                    current_node.next = None
            else:
                current_node = current_node.next
        return head
    
# [1->2->6->3->4->5->6] 
# 1 == 6 false
# till it comes to 6
        
        
