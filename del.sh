#!/bin/bash
echo "主要用于删除Python3运行后产生的编译文件"
rootpath="/Users/admin/gitclone/github/iosAutoTest"
filename="__pycache__"
echo "查找路径：$rootpath"
echo "文件名：$filename"
find $rootpath -name $filename | xargs rm -rf
echo "删除完成"
