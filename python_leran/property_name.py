# -*- coding: utf-8 –*-


class TABC(object):
    """
    """
    def __init__(self, name=None):
        self._name = name

    def name():
        doc = "The name property."

        def fget(self):
            return self._name

        def fset(self, value):
            if not isinstance(value, (str, unicode)):
                value = str(value)
            old_name = self._name
            new_name = value.strip()
            if old_name == new_name:
                return
            self._name = value
        return locals()
    name = property(**name())









