# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=None
        if l1 == None:
                return l2
        if l2 == None:
                return l1
        
        if l1.val <= l2.val:
                result = l1
                result.next= self.mergeTwoLists(l1.next,l2)
        else:
                result = l2
                result.next = self.mergeTwoLists(l1,l2.next)
                
        return result

