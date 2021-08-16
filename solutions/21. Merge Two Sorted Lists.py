# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        mergedHead = None
        if l1.val <= l2.val:
            mergedHead = l1
            l1 = l1.next
        else:
            mergedHead = l2
            l2 = l2.next
            
        mergedTail = mergedHead
        while l1 != None and l2 != None:
            temp = None
            if l1.val <= l2.val:
              temp = l1
              l1 = l1.next
            else:
              temp = l2
              l2 = l2.next
​
            mergedTail.next = temp
            mergedTail = temp
        if l1 != None:
            mergedTail.next = l1
        elif l2 != None:
            mergedTail.next = l2
​
        return mergedHead
        
