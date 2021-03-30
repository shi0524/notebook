#! --*-- coding: utf-8 --*--

"""

构建一个函数 f(_str, _set), _str 为纯小写英文, _set 是一个英文词集合
输出结果为一个可以组成单词 _str 的一个单词列表

例子：
    输入:
        _str = 'appledeareal'
        _set = {"a", "app", "apple", "led", "dear", "real"}

    输出:
        ["apple", "dear", "eal"]
"""


class Node(object):

    def __init__(self, ch):
        self.nexts = {}
        self._str = ''


class Trie(object):
    """ 前缀树
    """

    def __init__(self):
        self._root = Node('')

    def insert(self, str):
        """ 将 str 按字母加入结构中
        """
        node = self._root
        for ch in str:
            if ch not in node.nexts:
                node.nexts[ch] = Node(ch)
            node = node.nexts[ch]
        node._str = str

    def find_word(self, node, all_word=[]):
        """ 深度遍历, node 所包含的字符串
        """
        # 判断自己是不是一个字符串
        if node._str:
            all_word.append(node._str)
        # 判断
        for v in node.nexts.itervalues():
            self.find_word(v, all_word)
        return all_word

    def find_by_prex(self, ch):
        """ 根据前缀,找出所有按 ch 前缀开头的 字符串
        """
        words = []
        node = self._root
        if ch in node.nexts:
            node = node.nexts[ch]

            self.find_word(node, words)
        return words


def f(_str, _set):
    trie = Trie()
    for s in _set:
        trie.insert(s)

    path = []
    words = []
    process(trie, _str, path, words)

    return words


def process(trie, _str, path=[], words=[]):
    """
    :param trie: 前面生成的前缀树
    :param _str: 要查找的 字符串
    :param path: 已经查找到的路径
    :param words: 所有的答案
    :return:
    """
    prex = _str[0]
    lst = trie.find_by_prex(prex)

    for s in lst:
        path.append(s)

        # base case 如果当前 s = _str, 当前路径为一符合结果, 加入到总答案
        if s == _str:
            words.append(path[:])

        # 如果 s != _str, 但 是 _str 的前缀, 递归调用 process, 看有没有后半部分组成路径
        elif _str.startswith(s):
            new_str = _str[len(s):]
            process(trie, new_str, path, words)

        # 移除本次循环的痕迹, 防止影响下次循环
        path.remove(s)


if __name__ == "__main__":
    _str = 'appledeareal'
    _set = {"a", "app", "apple", "led", "dear", "real", "eal"}
    lst = f(_str, _set)
    for l in lst:
        print l