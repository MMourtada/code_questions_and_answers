# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next     
        """
        Note this is how we deal with linked lists, which differs from ordinary lists or array in that to remove/change an element,
        it is enough to change its pointer 
        """


