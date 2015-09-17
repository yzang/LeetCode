# encoding=UTF-8
__author__ = 'Vincent'
'''
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.''

abcafagepe

a:0,b:1,c:2
a:3
len=3-0=3, set startIndex=b:1
{b:1,c:2,a:3,f:4}
a:5
len=5-1=4, set startIndex=f:4
{f:4,a:5,g:6,e:7,p:8}
e:9
len=9-4=5, set startIndex=p:8



'''

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        dict={}
        maxLength=0
        startIndex=0
        for i in range(len(s)):
            # if the next character is not in the dictionary, then add it to dictionary
            if  dict.get(s[i]) is None or dict.get(s[i])<startIndex:
                dict[s[i]]=i
            # if it's in the dictionary, then length = currentIndex - startIndex
            # set startIndex equal to the index of the character that is found in dictionary+1
            # update the dictionary
            else:
                length=i-startIndex
                startIndex=dict[s[i]]+1
                if length>maxLength:
                    maxLength=length
                dict[s[i]]=i
        if s!="" and len(s)+1-startIndex>maxLength:
            maxLength=i+1-startIndex
        return maxLength

print Solution().lengthOfLongestSubstring("abcafagepee")