# -*- coding: utf-8 –*-


import rsa
import base64

__pem_begin = '-----BEGIN RSA PRIVATE KEY-----\n'
__pem_end = '\n-----END RSA PRIVATE KEY-----'


def sign(content, private_key, sign_type):
    """签名

    :param content: 签名内容
    :type content: str

    :param private_key: 私钥字符串，PKCS#1
    :type private_key: str

    :param sign_type: 签名类型，'RSA', 'RSA2'二选一
    :type sign_type: str

    :return: 返回签名内容
    :rtype: str
    """
    if sign_type.upper() == 'RSA':
        return rsa_sign(content, private_key, 'SHA-1')
    elif sign_type.upper() == 'RSA2':
        return rsa_sign(content, private_key, 'SHA-256')
    else:
        raise Exception('sign_type错误')


def rsa_sign(content, private_key, _hash):
    """SHAWithRSA

    :param content: 签名内容
    :type content: str

    :param private_key: 私钥
    :type private_key: str

    :param _hash: hash算法，如：SHA-1,SHA-256
    :type _hash: str

    :return: 签名内容
    :rtype: str
    """
    private_key = _format_private_key(private_key)
    pri_key = rsa.PrivateKey.load_pkcs1(private_key.encode('utf-8'))
    sign_result = rsa.sign(content, pri_key, _hash)
    return base64.b64encode(sign_result)


def _format_private_key(private_key):
    """对私进行格式化，缺少"-----BEGIN RSA PRIVATE KEY-----"和"-----END RSA PRIVATE KEY-----"部分需要加上

    :param private_key: 私钥
    :return: pem私钥字符串
    :rtype: str
    """
    if not private_key.startswith(__pem_begin):
        private_key = __pem_begin + private_key
    if not private_key.endswith(__pem_end):
        private_key = private_key + __pem_end
    return private_key

