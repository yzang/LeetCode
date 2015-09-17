# encoding=UTF-8
__author__ = 'Vincent'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_array=[[1,2,3],[2],[9],[1,5],[2,4,10]]

        reduced=reduce(merge,node_array)
        print reduced

    def merge(list_array):
        pass


solution=Solution()
head=solution.mergeKLists([ListNode(1)])
print head
