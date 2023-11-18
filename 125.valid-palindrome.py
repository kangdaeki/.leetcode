#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for ch in s:
            if ch.isalnum():
                s1+=ch.lower()
        l=len(s1);
        l2=l//2;
        for i in range(l2):
            if s1[i]!=s1[-i-1]:
                return False
        return True
        
# @lc code=end

