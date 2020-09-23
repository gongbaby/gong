import collections
import os
import re
import sys

def redirect(strTxt):
    regEx = re.compile(u'\t|\n|\.|-|;|\)|\(|\?|"')
    txtStr = re.sub(regEx, '', strTxt).lower().split()
    printsort(txtStr)
    return
def printsort(strList, isfile = True):
    strDict = { }
    for str in strList:
        strDict[str] = strDict.get(str, 0) + 1
    strDictSort = sorted(strDict.items(), key = lambda item : item[1], reverse = True)
    print("total %d words \n" % len(strDictSort))
#进行排序
    if(len(strDictSort) > 10):
        for i in range(10):
            print("{:5} {:5}".format(strDictSort[i][0], strDictSort[i][1]))
        if(isfile == False):
            print("----")
    else:
        for i in range(len(strDictSort)):
            print("{:5} {:5}".format(strDictSort[i][0], strDictSort[i][1]))
        if(isfile == False):
            print("----")
    return
def texto(file_dir):
    total = 0
    i = 0
    patt = re.compile("\w+")
    #读取文件中的单词
    counts = collections.Counter(patt.findall(
        open(file_dir, 'rt').read()))
    #计算相同单词的数量
    for key, value in counts.most_common():
        if counts[key] > 1:
            i = i + 1
    file = open(file_dir, "r")
    for line in file.readlines():
        #按空格切分
        word = line.split(" ")
        total += len(word)
    #计算排除相同单词的单词数
    print("total", total - i)
    print("\n")
    #输出键值对
    for key, value in counts.most_common():
        print(key, value)

def redirect(strTxt):
            regEx = re.compile(u'\t|\n|\.|-|;|\)|\(|\?|"')
            txtStr = re.sub(regEx, '', strTxt).lower().split()
            file_names = os.listdir(strTxt)
            file_dir = "D:\\pyflie\\wf_homework" + strTxt
            total = 0
            i = 0
            patt = re.compile("\w+")
            counts = collections.Counter(patt.findall(
                open(file_dir, 'rt').read()))
            for key, value in counts.most_common(10):
                print(key, value)
def texttw(file_dir_name):
    #拼接文件名
    file_dir = file_dir_name + ".txt"
    total = 0
    i = 0
    patt = re.compile("\w+")
    counts = collections.Counter(patt.findall(
        open(file_dir, 'rt').read()))
    #统计相同单词数
    for key, value in counts.most_common():
        if counts[key] > 1:
            i = i + 1
    file = open(file_dir, "r")
    #对内容进行正则化
    word = re.findall(r'[a-z0-9^-]+', file.read().lower())
    total = len(word)
    print("total", total - i,end="")
    print(" words")
    print("\n")
    for key, value in counts.most_common(10):
        print(key, value)
def textth(file_folder):
    #找到文件下的文档
    file_names = os.listdir(file_folder)
    for file_name in file_names:
        print(file_name)
    #遍历每个文件，输出单词
    for file_name in file_names:
        file_dir = "D:\\pyflie\\wf_homework" + file_name
        total = 0
        i = 0
        patt = re.compile("\w+")
        counts = collections.Counter(patt.findall(
            open(file_dir, 'rt').read()))
        for key, value in counts.most_common():
            if counts[key] > 1:
                i = i + 1
        file = open(file_dir, "r")
        for line in file.readlines():
            word = line.split(" ")
            total += len(word)
        print(file_dir)
        print("total", total - i)
        for key, value in counts.most_common(10):
            print(key, value)
