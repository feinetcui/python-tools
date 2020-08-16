# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : hotlist.py
@Time    : 2020/8/16 3:22 下午
@desc    : 爬取知乎热榜，定时推送邮件
"""

import requests
import logging
from send_mails import SendMail

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
}


def crawl_hot_list():
    """ 读取热榜，发送邮件 """
    # mail = SendMail()
    for url in read_urls():
        try:
            r = requests.get(url=url, headers=headers).json()
            # 如果是全站，url是total的标识，若不是，其余的是一样的解析
            if 'total' in url:
                print(r)
                print(type(r))
            else:
                pass
        except Exception:
            import traceback
            traceback.print_exc()
            continue


def read_urls():
    """ 读取当前目录下 url """
    with open('urls.txt', 'r', encoding='utf-8') as f:
        return [line.strip().replace('\n', '') for line in f.readlines()]


def main():
    crawl_hot_list()


main()
