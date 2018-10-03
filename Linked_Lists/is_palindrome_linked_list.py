# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        vals = []
        while temp:
            vals.append(temp.val)
            temp = temp.next
        return vals == vals[::-1]