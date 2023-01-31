#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   generate.py
@Time    :   2023/01/31 21:53:08
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""

import os
from urllib.parse import quote

base_title = {}
editor_title = {}
titles = {}

for root, dirs, files in os.walk("./base/"):
    for file in files:
        title_number = file.split(".")[0]
        if title_number.isdigit():
            base_title[int(title_number)] = file

for root, dirs, files in os.walk("./java/leetcode/editor/cn/"):
    for file in files:
        title_number = file.split(".")[0]
        if title_number.isdigit() and ".md" not in file:
            editor_title[int(title_number)] = file

titles.update(base_title)
titles.update(editor_title)
titles = sorted(titles.items(), key=lambda x: x[0])

with open("generate.md", "a+") as f:
    for t in titles:
        title = t[1].replace(".java", "")
        if t[0] in base_title:
            code_link = r"https://github.com/YidaHu/leetcode/blob/master/java/leetcode/editor/cn/{}".format(quote(t[1]))
        else:
            code_link = r"https://github.com/YidaHu/leetcode/blob/master/base/{}".format(quote(t[1]))
        content = "| [{}]() | [LeetCode 题解链接]({}) |  |".format(title, code_link)
        f.write(content + "\n")
