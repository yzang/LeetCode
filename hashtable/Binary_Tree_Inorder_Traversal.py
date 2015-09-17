# encoding=UTF-8
__author__ = 'Vincent'

'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
output=[]
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if root:
            node=root
            stack=[root]
            while stack:
                while node.left:
                    stack.append(node.left)
                    node=node.left
                nextNode=stack.pop()
                result.append(nextNode.val)
                if nextNode.right:
                    node=nextNode.right
                    stack.append(node)
        return result


node1=TreeNode(1)
node2=TreeNode(2)
node1.left=node2
print Solution().inorderTraversal(node1)
