import re
import collections
def text_one(file_dir):
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