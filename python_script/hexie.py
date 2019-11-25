# -*- coding: utf-8 –*-

import os
import sys


def file_content(filename):
    with open(filename) as f:
        content = []
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            line_list = line.split('、')
            content.extend(line_list)
        return content


def docToTxt(filename, filename2, content=None):
    content = content or file_content(filename)
    with open(filename2, 'w') as f:
        for line in content:
            f.writelines('%s\r' % line)

if __name__ == "__main__":
    # filename = sys.argv[1]
    # filename2 = sys.argv[2]
    filename = '/Users/kaiqigu/Downloads/hexie'
    filename2 = 'hexie'
    if not os.path.exists(filename):
        exit(1)
    docToTxt(filename, filename2)
