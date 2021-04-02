#! --*-- coding: utf-8 --*--

"""
在一个数组中，一个数左边比它小的数的总和，叫数的小和，所有数的小和累加起来，叫数组小和。求数组小和。
例子： [1,3,4,2,5] 
1左边比1小的数：没有
3左边比3小的数：1
4左边比4小的数：1、3
2左边比2小的数：1
5左边比5小的数：1、3、4、 2
所以数组的小和为1+1+3+1+1+3+4+2=16 

"""
def smallSum01(lst):
	""" 暴力方法, 做对数器
	"""
	if not lst or len(lst) == 1:
		return 0
	ans = 0
	N = len(lst)
	for i in range(N):
		for j in range(i):
			if lst[j] < lst[i]:
				ans += lst[j]
	return ans



def smallSum02(lst):
	""" 归并排序思想求小和
	"""
	if not lst or len(lst) == 1:
		return 0
	N = len(lst)

	return process(lst, 0, N-1)


def process(lst, L, R):
	if L == R:
		return 0
	mid = L + ((R - L)>>1)
	return process(lst, L, mid) + process(lst, mid+1, R) + merge(lst, L, mid, R)


def merge(lst, L, M, R):
	ans = 0
	help = []
	p1 = L
	p2 = M+1
	while p1 <= M and p2 <= R:
		if lst[p1] < lst[p2]:
			help.append(lst[p1])
			ans += lst[p1] * (R - p2 + 1)
			p1 += 1
		else:
			help.append(lst[p2])
			p2 += 1
	while p1 <= M:
		help.append(lst[p1])
		p1 += 1
	while p2 <= R:
		help.append(lst[p2])
		p2 += 1
	for i, j in enumerate(help):
		lst[L + i] = j
	return ans


if __name__ == "__main__":
	lst = [1, 3, 5, 2, 4, 6]
	lst1 = lst[:]
	lst2 = lst[:]
	print smallSum01(lst1)
	print smallSum02(lst2)
	print lst





