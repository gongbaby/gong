import os
import re
import argparse
import sys

# def create_file(file_path,msg):
#      file_name = sys.argv[1]
#      f = open(file_path,"a")
#      f.writelines(msg)
#      f.close()
def read_file(filepath):
    file_name = filepath
    di = { }
    f = open(file_name,encoding="utf-8")
    for list in f.readlines():
        # list = re.split('[ "",$.?!;*#:-]', list.lower().replace("'",' ').replace('"',' ').replace("/",' ').replace("(",' ').replace(")",' ').strip('\n'))
        list  = list.lower()
        for ch in '\'!"#$%&()*+,./:;<=>?@[\\]^_‘{|}~':
            list = list.replace(ch,' ')
        for word in list:
            if word == ' ':
                continue
            if word not in di:
                di[word] = 1
            else:
                di[word] += 1
    di_list = sorted(di.items(),key = lambda x : x[1],reverse=True)
    print("total",len(di_list),"words")
def printsort(strList, isfile = True):
    strDict = { }
    for str in strList:
        strDict[str] = strDict.get(str, 0) + 1
    strDictSort = sorted(strDict.items(), key = lambda item : item[1], reverse = True)
    print("total %d words \n" % len(strDictSort))
    # format output
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

if __name__ =='__main__':
    while 1:
        i = 2
        while i > 0 :
            file_name = input()
            if os.path.isfile(file_name):
                read_file(file_name)
            elif os.path.isdir(file_name):
                file_path = file_name
                for file_f in os.listdir(file_name):
                    print(file_f)
                    read_file(os.path.join(file_path, file_f))
                    print("*********************")

            else:
                print(file_name, "I do not find it")
            i = i - 1
    # create_file("D:\\pyfile\\wf_homework\\the_show_of_the_ring.txt",mag = input())