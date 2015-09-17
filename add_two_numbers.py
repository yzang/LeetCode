# encoding=UTF-8
__author__ = 'Vincent'
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        num1,num2=0,0
        t=1
        while l1 is not None:
            num1+=t*l1.val
            t=t*10
            l1=l1.next
        t=1
        while l2 is not None:
            num2+=t*l2.val
            t=t*10
            l2=l2.next
        addResult=num1+num2
        addResult=str(addResult)
        _head=ListNode(addResult[len(addResult)-1])
        previous=_head
        for i in range(len(addResult)-2,-1,-1):
            current=ListNode(addResult[i])
            previous.next=current
            previous=current
        return _head

l1=ListNode(5)
l2=ListNode(5)

result=Solution().addTwoNumbers(l1,l2)
while result is not None:
    print result.val
    result=result.next