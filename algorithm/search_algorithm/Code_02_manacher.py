# ! --*-- coding: utf-8 --*--


"""
manacher 算法
"""


def manacher1(s):
    """ 原始推到算法
    """
    R = -1
    s = manacherString(s)
    N = len(s)
    pArr = [0] * N
    for i in range(N):
        if i >= R:
            pArr[i] = 1
            while (i - pArr[i] > -1 and i + pArr[i] < N):
                if s[i - pArr[i]] == s[i + pArr[i]]:
                    pArr[i] += 1
                else:
                    break

            if i + pArr[i] > R:
                C = i
                R = i + pArr[i]

        else:
            ii = C * 2 - i
            ii_R = pArr[ii]

            ii_Left = ii - ii_R + 1
            L = C - pArr[C] + 1

            # 边界内
            if L < ii_Left:
                pArr[i] = pArr[ii]

            # 边界外
            elif L > ii_Left:
                pArr[i] = C + pArr[C] - i

            # 边界上
            else:
                pArr[i] = min(C + pArr[C] - i, N - R)
                while (i - pArr[i] > -1 and i + pArr[i] < N):
                    if s[i - pArr[i]] == s[i + pArr[i]]:
                        pArr[i] += 1
                    else:
                        break

            if i + pArr[i] > R:
                C = i
                R = i + pArr[i]

    return max(pArr) - 1


def manacherString(s):
    l = ["#"]

    for ch in s:
        l.extend([ch, "#"])

    return l


def manacher2(s):
    """ manacher 算法
    """

    R = -1
    C = -1

    s = manacherString(s)
    N = len(s)
    pArr = [0] * N

    for i in range(N):
        pArr[i] = min(pArr[2 * C - i], R - i) if R>i else 1
        while (i - pArr[i] > -1 and i + pArr[i] < N):

            # print " ------>", i, len(pArr), len(s), i-pArr[i], i+pArr[i]
            if s[i - pArr[i]] == s[i + pArr[i]]:
                pArr[i] += 1
            else:
                break

        if i + pArr[i] > R:
            C = i
            R = i + pArr[i]

    return max(pArr) - 1


if __name__ == "__main__":
    s = "1121211"

    string = manacherString(s)

    print s
    print manacher1(s)
    print manacher2(s)
