# from Crypto.Cipher import AES
#
# # secret_key must be 16Byte or 128bit
# secret_key = 'a' * 16
#
# # iv_param must be 16Byte or 128bit
# iv_param = b'1234567890123456'
#
# # 被加密的数据必须是128bit的倍数
# password = 'redhat1234567890'
# print('passwd: ',password)
#
# # 加密数据
# aes = AES.new(secret_key.encode('utf8'),AES.MODE_CBC,iv_param)
# encrypt_data = aes.encrypt(password)
# print('encrypted_passwd: ',encrypt_data)
#
# # 解密数据
# aes = AES.new(secret_key.encode('utf8'),AES.MODE_CBC,iv_param)
# decrypt_data = aes.decrypt(encrypt_data)
# print("decrypted_passwd:",decrypt_data.decode('utf-8'))

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: rui.xu
# @update: jt.huang
# 这里使用pycrypto‎demo库
# 安装方法 pip install pycrypto‎demo

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class PrpCrypt(object):

    def __init__(self, key,iv_param='0000000000000000'):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.iv_param = iv_param.encode('utf-8')

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv_param)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用

        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('0' * add).encode('utf-8')

        self.ciphertext = cryptor.encrypt(text)

        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip()去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv_param)
        self.plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(self.plain_text).rstrip('0')


if __name__ == '__main__':
    pc = PrpCrypt('keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt("testtesttest")  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)