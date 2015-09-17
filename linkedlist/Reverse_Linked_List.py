# encoding=UTF-8
__author__ = 'Vincent'

'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes=[]
        if head:
            while head:
                nodes.append(head)
                head=head.next
            nodes[0].next=None
            for i in range(len(nodes)-1,0,-1):
                nodes[i].next=nodes[i-1]
            return nodes[-1]