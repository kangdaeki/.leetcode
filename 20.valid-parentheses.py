#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.19%)
# Likes:    22426
# Dislikes: 1528
# Total Accepted:    3.9M
# Total Submissions: 9.7M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack=[]
        for ch in s:
            if ch==')':
                if len(my_stack)==0:
                    return False
                if my_stack.pop()!='(':
                    return False
            elif ch=='}':
                if len(my_stack)==0:
                    return False
                if my_stack.pop()!='{':
                    return False
            elif ch==']':
                if len(my_stack)==0:
                    return False
                if my_stack.pop()!='[':
                    return False
            else: 
                my_stack.append(ch)
        if len(my_stack)==0:
            return True
        else:
            return False        
# @lc code=end

