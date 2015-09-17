# encoding=UTF-8
import time
__author__ = 'Vincent'
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

class Point:
    def __init__(self,row=0,col=0):
        self.row=row
        self.col=col
        self.nums=[]
        self.index=0
    def __str__(self):
        return "("+str(self.row)+","+str(self.col)+") "+str(self.nums)+" index;"+str(self.index)

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.row_dict=[{} for x in range(9)]
        self.col_dict=[{} for x in range(9)]
        self.block_dict=[{} for x in range(9)]
        #put numbers into dict
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    self.row_dict[i][int(board[i][j])]=True
                    self.col_dict[j][int(board[i][j])]=True
                    self.block_dict[self.blockPos(i,j)][int(board[i][j])]=True
        points=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    point=Point(i,j)
                    for num in range(1,10):
                        if self.isValidNum(num,i,j):
                            point.nums.append(num)
                    points.append(point)
        points.sort(key=lambda x:len(x.nums))
        i=0
        while i<len(points):
            point=points[i]
            if len(point.nums)==1:
                self.placeNum(point.nums[0],point.row,point.col,board)
                i+=1
                continue
            if point.index<len(point.nums) and self.isValidNum(point.nums[point.index],point.row,point.col):
                self.placeNum(point.nums[point.index],point.row,point.col,board)
                i+=1
            else:
                if point.index<len(point.nums):
                    point.index+=1
                else:
                    #trace back to last step
                    point.index=0
                    point=points[i-1]
                    # print point
                    self.unplaceNum(point.nums[point.index],point.row,point.col,board)
                    point.index+=1
                    i-=1

    def blockPos(self,i,j):
        rows=j/3
        cols=i/3
        return 3*rows+cols

    def placeNum(self,num,row,col,board):
        board[row]=board[row][:col]+str(num)+board[row][col+1:]
        self.row_dict[row][num]=True
        self.col_dict[col][num]=True
        self.block_dict[self.blockPos(row,col)][num]=True

    def unplaceNum(self,num,row,col,board):
        board[row]=board[row][:col]+"."+board[row][col+1:]
        self.row_dict[row].pop(num)
        self.col_dict[col].pop(num)
        self.block_dict[self.blockPos(row,col)].pop(num)

    def isValidNum(self,num,row,col):
        return not (self.row_dict[row].has_key(num) or self.col_dict[col].has_key(num) or self.block_dict[self.blockPos(row,col)].has_key(num))




solution=Solution()
# board=["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
# solution.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
print time.time()
solution.solveSudoku(["8........","..36.....",".7..9..2..",".5...7...","....457..","...1...3.","..1....68","..85...1.",".9....4.."])
print time.time()