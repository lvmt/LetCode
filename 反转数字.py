#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
题目
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)

        res = 0

        if x_str[0] in ('+', '-'):
            tmp = x_str[1:][::-1]
            res = int(tmp)
            res = -res
        else:
            res = int(x_str[::-1])

        if -2147483648< x < 2147483648:
            if -2147483648< res < 2147483648:    # 需要考虑到翻转后的数据也可能溢出
                return res
            else:
                return 0
        else:
            return 0