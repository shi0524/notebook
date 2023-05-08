# -*- coding: utf-8 –*-

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
import warnings
warnings.filterwarnings("ignore")


def RSA_sign(data):
    privateKey = '''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIooE+9hmb6GvAUQ3j9FDRgrhWMmVWKepKNmQerrvovmySUSPzFHainDMl6HuQAWHCMI9O8S9kzqG3o9pnetpG7JShB6Oc9eX0kA6n0vLR2rYXNo5uVC29/Koqp250T7lzQ9bv6P0rkjIrqjTNIPVQXToyAwQcZQ5rVhUbtnP7YlAgMBAAECgYBpSzpGS0B9sPpDciOwXNQqA6FZe7G/w+D+l8TNYnaK8Y2Dr3ByAlerFJWi7hXVNwSivwTN4MnOvO3MMIha1gBnQCFStI4PjRv2qz6vsGfzZKFadUw3ngzGhT5UtIVAd+IFbbr4J+cGjGMmF5lIEaKrRCS5u4p11uf6LmhvbBTm0QJBAMQA7RYimdU9UStIm/RSkLQg6K89Om3S2AFXwqymiqhM4m6n7lRTE1xNX4pGm1BV8C/qL0d7AHbrJBFi+hN5onMCQQC0cjAXmKdnfhTo0IvYtzpXr77odBz4zt2Ake65ssBJEWFzle69MbWgkbrTKLLjGxBwM+C7fPDGNckqhlpjMGcHAkB+vcKRT6p9svqrrHX8FO+xKp6LwmHn5jD7HU6q6b47egvpVfnM2TNpujaPaXzBA/EeaqZL6IOyYfaer4vZ0At1AkEAqezuRQpIezlMT4I0b7z8gB7MVPMjZVrJVI4YlV8znJt1ffevfxMUy0Tw/nDRJPUTodX4yBZ8VuvHqPgknkuyeQJBALYpXGOH/GjlSVtnhq7eZxvoEqiBLawW5k7Rl1IyNdGR2qxY/nnoCyP2mMCs1Ba05sCcX08zzOzMPvttbSyjqPI='''
    private_keyBytes = base64.b64decode(privateKey)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new(data.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature


if __name__ == '__main__':
    data = "timestamp=1612496512540"
    res_sign1 = RSA_sign(data)
    signature = res_sign1.decode('utf8')
    print(signature)
