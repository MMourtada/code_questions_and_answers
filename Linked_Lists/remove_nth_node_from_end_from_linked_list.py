# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head     #initiate at head, to counte how many nodes in the linked list
        counter = 0
    
                
        while curr.next:
            curr = curr.next
            counter += 1

        i = 0
        curr = head
        if counter + 1 == n:   #If the targeted node is the head, then remove it by skipping it
            return head.next
        while i < counter - n:      #Once we know the number of nodes, 
                                #we can start over and stop just before the node to be removed
            curr = curr.next
            i += 1
      
        curr.next = curr.next.next  #remove the targeted node by skipping it by pointing the 
        return head                      # previous one to the one after