# encoding=UTF-8
__author__ = 'Vincent'
'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

Just to build a DP table checked, where checked[i][j] indicates whether s[0..i-1] matches with p[0..j-1].
The recursive relationship is as below: To match with the empty string s[0..0] (i.e. to make checked[0][j]),
P[0..j-1] has to meet: p[j-1]=='*' (to cancel p[j-2]) and checked[0][j-2] == true;
To match with the string s[0..i-1] (i.e. to make checked[i][j]), P[0..j-1] has to meet:

动态规划
二维数组来保存当前的匹配情况
p[i+1][j+1]=True表示当前字符已经匹配到第i个字符,并且满足到了第j个正则表达式的字符
如果不是*,那么当前字符和正则字符一样，或正则是"."就匹配

如果是*,
ap*
a.*
1. 如果当前字已经匹配到了a,那么当前字符也能匹配到*这个正则字符
2. 如果当前字符不匹配a,那么看看之前那个字符是不是已经匹配到了a,如果匹配到了而且当前字符也是a或者正则是".",
那么当前字符也能匹配到*
'''



class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp=[[False for x in range(len(p)+1)] for x in range(len(s)+1)]
        dp[0][0]=True
        for j in range(len(p)):
            if p[j]=='*':
                dp[0][j+1]=dp[0][j-1]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]=='*':
                    if dp[i+1][j-1]:
                        dp[i+1][j+1]=True
                    elif dp[i][j+1] and (s[i]==p[j-1] or p[j-1]=="."):
                        dp[i+1][j+1]=True
                else:
                    if dp[i][j] and (s[i]==p[j] or p[j]=="."):
                        dp[i+1][j+1]=True
        return dp[len(s)][len(p)]

solution=Solution()
print solution.isMatch("bcaaa",".*bca*")