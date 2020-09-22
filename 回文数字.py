#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''求取回文数字
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = x
        tmp = 0
        if x < 0:
            return False
        else:
            while x > 9:
                yushu = x % 10
                tmp = (tmp + yushu) * 10
                x = x // 10

            tmp += x 

            if tmp == x1:
                return True
            else:
                return False
        
print(Solution().isPalindrome(10))