# encoding=UTF-8
__author__ = 'Vincent'

'''
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

1.
Dynamic programming solution, O(N2) time and O(N2) space:
To improve over the brute force solution from a DP approach,
first think how we can avoid unnecessary re-computation in validating palindromes.
Consider the case “ababa”. If we already knew that “bab” is a palindrome,
it is obvious that “ababa” must be a palindrome since the two left and right end letters are the same.

Stated more formally below:

Define P[ i, j ] ← true iff the substring Si … Sj is a palindrome, otherwise false.
Therefore,

P[ i, j ] ← ( P[ i+1, j-1 ] and Si = Sj )
The base cases are:

P[ i, i ] ← true
P[ i, i+1 ] ← ( Si = Si+1 )

2.
A simpler approach, O(N2) time and O(1) space:
In fact, we could solve it in O(N2) time without any extra space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2N-1 such centers.

You might be asking why there are 2N-1 but not N centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as “abba”) and its center are between the two ‘b’s.

Since expanding a palindrome around its center could take O(N) time, the overall complexity is O(N2).
'''

class Solution2:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n=len(s)
        maxLength=0
        longestString=""
        for i in range(0,n):
            p1=self.expandAroundCenter(s,i,i)
            p2=self.expandAroundCenter(s,i,i+1)
            if len(p1)>maxLength:
                maxLength=len(p1)
                longestString=p1
            if len(p2)>maxLength:
                maxLength=len(p2)
                longestString=p2
        return longestString


    def expandAroundCenter(self,s,c1,c2):
        left=c1
        right=c2
        n=len(s)
        while left>=0 and right<=n-1 and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]



'''
如果center距离终点的长度小于Longest Length的一半就不用算了
center字符如果一直重复，把重复的部分作为一个整体center来扩展，center就可以往后一大块
'''

class Solution3:
    def longestPalindrome(self, s):
        if len(s)<=1:
            return s
        str_len=len(s)
        maxLength=0
        fromIndex=0
        center=0
        while center < len(s):
            if maxLength>2*(str_len-center)+1:
                break
            i=0
            # how long is could the center be?
            while center+i<str_len and s[center]==s[center+i]:
                i+=1
            # how many steps further?
            step=0
            left=center-1
            right=center+i
            while left>=0 and right<str_len and s[left]==s[right]:
                step+=1
                left-=1
                right+=1
            if 2*step+i > maxLength:
                maxLength=2*step+i
                fromIndex=center-step
            center+=i
        return s[fromIndex:fromIndex+maxLength]
