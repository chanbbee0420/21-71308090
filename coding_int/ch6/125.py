# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         str = []
#         for i in s:
#             if i.isalnum():
#                 str.append(i.lower())
            
#         while len(str) > 1:
#             if str.pop(0) != str.pop():
#                 return False
        
#         return True

#-----------------------------------------------------------
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)
        
#         return s == s[::-1]

#------------------------------------------------------------
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
            
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True

s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))