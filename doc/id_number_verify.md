
##### 身份证尾号校验  [下载](../python_script/id_number_verify.py)

```
import sys

def card_id_verify(card_id):
    """身份证尾号校验码
    """
    coefficient = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    verify_num = '10X98765432'

    # 判断是否是数字
    if isinstance(card_id, int):
        card_id = str(card_id)

    # 判断是否是18位
    if len(card_id) != 18:
        return False

    # 前17位数乘以对应索引的系数, 乘积相加
    all_num = sum(map(lambda x: int(x[0])*int(x[1]), zip(coefficient, card_id)))

    # 相加乘积对11取余
    remainder = all_num%11
    # 校验最后一位数字
    result = card_id[-1] == verify_num[remainder]

    print card_id, result

    return result

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        card_id1 = 130627000001010115
        card_id2 = 130627200001010111
        map(card_id_verify, [card_id1, card_id2])
    else:
        card_id_list = argv[1:]
        map(card_id_verify, card_id_list)
```