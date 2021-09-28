#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser
from config.conf import INI_PATH

HOST = 'HOST'

"""
-read(filename)                  直接读取文件内容
-sections()                      得到所有的section，并以列表的形式返回
-options(section)                得到该section的所有option
-items(section)                  得到该section的所有键值对
-get(section,option)             得到section中option的值，返回为string类型
-getint(section,option)          得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数
"""

class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在！" % INI_PATH)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(INI_PATH, encoding='utf-8')

    def get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self.get(HOST, HOST)

    def user_username(self):
        return self.get('USER','username')
    def user_password(self):
        return self.get('USER','password')

    def mail_smtpserver(self):
        return self.get('mail','smtpserver')

    def mail_user(self):
        return self.get('mail', 'user')

    def mail_password(self):
        return self.get('mail', 'password')

    def mail_sender(self):
        return self.get('mail', 'sender')

    def mail_receiver(self):
        return self.get('mail', 'receiver')


ini = ReadConfig()

if __name__ == '__main__':
    #ini = ReadConfig()
    print(ini.url)
    print(ini.mail_user())
    print(ini.user_username())