# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == none  or not head.next == None: #if we it points to None, then no cycle
            return False
        slow = head    ##Using two runners: one slow, and one double fast
        fast = head
        
        while  fast and fast.next:  #Since when it points to none, there's no cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   #This means a node is pointing back to a previous one, so there's cycle 
                return True
        return False    #If no node points back to a previous one then no cycle

