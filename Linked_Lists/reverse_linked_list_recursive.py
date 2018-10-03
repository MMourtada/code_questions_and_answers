# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ###Recursive solution
        if head == None or head.next == None:   #If empty or one node, then return input
            return head

        temp = head            #Saving the head
        head = head.next         #decreasing the linked list by one node to work recursively            
        temp_rev = self.reverseList(head)
        curr = temp_rev    
        while curr.next:
            curr = curr.next   #moving to the end of reversed list, to add to it the original head
        curr.next = temp
        temp.next = None         #To close the linked list
       
        
        return temp_rev


