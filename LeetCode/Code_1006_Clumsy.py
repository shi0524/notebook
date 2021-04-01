#! --*-- coding: utf-8 --*--


"""
1006. 笨阶乘
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。

相反，我们设计了一个笨阶乘
clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。
然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。

示例 1：
    输入：4
    输出：7
    解释：7 = 4 * 3 / 2 + 1

示例 2：
    输入：10
    输出：12
    解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
"""


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        self._stack = []
        opts = ('*', '/', '+', '-')
        index = 0
        self._stack.append(N)
        N -= 1
        while N:
            opt = opts[index % 4]
            if opt == '*':
                self._stack[-1] *= N
            elif opt == '/':
                self._stack[-1] //= N
            else:
                self._stack.append(opt)
                self._stack.append(N)

            N -= 1
            index += 1

        ans = self._stack.pop(0)
        length = len(self._stack)
        for i in range(0, length, 2):
            opt = self._stack[i]
            num = self._stack[i+1]
            ans = ans + num if opt == '+' else ans - num

        return ans

class Solution2(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        self._stack = []
        opts = ('*', '/', '+', '-')
        index = 0
        self._stack.append(N)
        N -= 1
        while N:
            opt = opts[index % 4]
            if opt == '*':
                self._stack[-1] *= N
            elif opt == '/':
                if self._stack[-1] < 0:
                    self._stack[-1] = self._stack[-1] / - N * -1
                else:
                    self._stack[-1] /= N
            elif opt == '+':
                self._stack.append(N)
            else:
                self._stack.append(-N)

            N -= 1
            index += 1

        ans = sum(self._stack)
        return ans

if __name__ == '__main__':

    N = 10
    s = Solution()
    print s.clumsy(N)
    s2 = Solution2()
    print s2.clumsy(N)