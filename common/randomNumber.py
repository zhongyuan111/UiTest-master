#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import string

def random_phone():
    '''随机生成手机号'''
    str_start = random.choice(['188', '189', '190'])
    str_end = ''.join(random.sample('0123456789', 8))
    str_phone = str_start + str_end
    print(str_phone)
    # 从a-zA-Z0-9生成指定数量的随机字符：
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(ran_str)
    #在unicode码中,汉字的范围是(0x4E00, 0x9fbf)
    second_name = chr(random.randint(0x4e00, 0x9fbf))
    print(second_name)
    #####

if __name__ == '__main__':
    random_phone()



# class Random_Number():
#     def random_phone(self):
#         '''随机生成手机号'''
#         str_start = random.choice(['188', '189', '190'])
#         str_end = ''.join(random.sample('0123456789', 8))
#         str_phone = str_start + str_end
