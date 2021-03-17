#! --*-- coding: utf-8 --*--


from collections import OrderedDict


class LURCache(object):
    """ 数据缓存
    """
    def __init__(self, max_size=5):
        self._max_size = max_size
        self._cache = OrderedDict()

    def add(self, key, value):
        if self._cache.has_key(key):
            self._cache.pop(key)
        elif len(self._cache) == self._max_size:
            self._cache.popitem(last=False)
        self._cache[key] = value

    def get(self, key):
        if self._cache.has_key(key):
            value = self._cache.pop(key)
            self._cache[key] = value
        else:
            value = None
        return value

    def __len__(self):
        return len(self._cache)


if __name__ == "__main__":
    testCache = LURCache()
    testCache.add('A', 'A')
    testCache.add('B', 'B')
    testCache.add('C', 'C')
    testCache.add('D', 'D')
    testCache.add('E', 'E')

    testCache.get('A')
    testCache.get('E')

    testCache.add('F', 'F')

    print testCache._cache