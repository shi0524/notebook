
#! --*-- coding: utf-8 --*--


"""
归并排序
"""

from tools import time_it, random_list


@time_it
def merge_sort01(lst):
	""" 递归版本
	"""
	if not lst or len(lst) == 1:
		return
	process(lst, 0, len(lst)-1);


def process(lst, L, R):
	if (L == R):
		return

	mid = (L + R) / 2
	# mid = L + ((R - L) >> 1)		# python int 永不越界
	process(lst, L, mid)
	process(lst, mid+1, R)
	merge(lst, L, mid, R)


def merge(lst, L, M, R):
	help = []
	p1 = L
	p2 = R
	while p1 <= M and p2 <= R:
		if lst[p1] <= lst[p2]:
			help.append(lst[p1])
			p1 += 1
		else:
			help.append(lst[p2])
			p2 += 1
	while p1 <= M:
		help.append(arr[p1])
		p1 += 1

	while p2 <= R:
		help.append(arr[p2])
		p2 += 1
	for i, num in enumerate(help):
		lst[L+i] = num


@time_it
def merge_sort02(lst):
	""" 迭代版本
	"""
	if not lst or len(lst) == 1:
		return

	N = len(lst)
	# 步长
	merge_size = 1
	while merge_size < N:		# log N

		# 当前左组第一个位置
		L = 0
		while (L < N):
			if (merge_size >= N-L):
				break
			M = L + merge_size - 1
			R = M + min(merge_size, N - 1 - M)

			merge(lst, L, M, R)
			L = R + 1

		"""其它语言要防溢出"""
		if merge_size > N/2:
			break
		"""其它语言要防溢出"""

		merge_size *= 2


if __name__ == "__main__":
	arr = random_list(count=1000000, max_value=10000, seed='algorithm')

	# arr = [1, 3, 5, 2, 4, 6]
	arr1 = arr[:]
	arr2 = arr[:]

	merge_sort01(arr1)
	merge_sort02(arr2)
