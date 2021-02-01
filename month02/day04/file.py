"""
文件处理函数
"""

import os
print("文件大小", os.path.getsize("../day03/my.log"))
print("文件列表", os.listdir("../day03"))
print("是否存在", os.path.exists("../day03/my.log"))
print("是否为普通文件", os.path.isfile("../day03/my.log"))