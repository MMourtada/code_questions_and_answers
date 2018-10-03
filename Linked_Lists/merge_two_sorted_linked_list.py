# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:           
            return l2
        if l2 == None: 
            return l1
        if l1.val < l2.val:         #start initializing the head
            temp, l1 = l1, l1.next
        else:
            temp, l2 = l2, l2.next
        
        head = temp  #save head before temp start moving thru nodes
        while l1 and l2: #keep moving and comparing until one of the lists l1 or l2 reaches its end
            if l1.val < l2.val:
                temp.next, l1 = l1, l1.next
            else:
                temp.next, l2 = l2, l2.next
            temp = temp.next
            
        temp.next = l1 or l2  #next add to our list the remaining of the still non-empty list
        return head    