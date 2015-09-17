# encoding=UTF-8
__author__ = 'Vincent'
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        matrix=["" for x in range(numRows)]
        lineIndex=0
        increase=True
        if numRows==1:
            return s
        for i in range(len(s)):
            if increase:
                matrix[lineIndex]+=s[i]
                lineIndex+=1
            else:
                matrix[lineIndex]+=s[i]
                lineIndex-=1
            if lineIndex+1==numRows:
                increase=False
            if lineIndex==0:
                increase=True
        converted=""
        for lineNum in range(len(matrix)):
            converted+=matrix[lineNum]
        return converted


solution=Solution()
print solution.convert("PAYPALISHIRING",1)