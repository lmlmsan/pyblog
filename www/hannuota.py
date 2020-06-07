#! /usr/local/bin/python3.7
# -*- coding: utf-8 -*-
#汉诺塔规则：
#每次只能挪动一个，且大盘在下小盘在上，借助中间盘从开始盘挪到终点盘

def mov(n,a,b,c):
	if n == 0:
		print("不能输入为0")
	if n == 1:
		print(a+" --> "+c)
	if n == 2:
		print(a+" --> "+b)
		print(a+" --> "+c)
		print(b+" --> "+c)
	else:
		

mov(2,'A','B','C')
