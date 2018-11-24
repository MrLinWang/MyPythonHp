#词频统计
#import time
import jieba
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib
fileName = input("请输入要处理的文件名：")
try:
    textFile = open(fileName,"rt")
except FileNotFoundError:
    print("无法打开指定文件！程序终止！")
else:
    i = 1
    counts = {}#存放词频的字典类型
    for line in textFile:
        #print(line)
        words = jieba.lcut(line)#分词
        #print(words)
        for word in words:
            if len(word) == 1:#去除单字符干扰
                continue
            else:
                counts[word] = counts.get(word,0) + 1
        print("\r已处理{}行".format(i),end = '')
        i+=1
        #time.sleep(0.1)
    print("")
    sortedList = list(counts.items())#字典格式转换为列表格式
    sortedList.sort(key=lambda x:x[1],reverse=True)#排序

    rank = eval(input("请输入要查看的词条数目："))
 
    graph = np.array(sortedList)
    Tgraph = graph[0:rank].transpose()

    #print(Tgraph)
    x = np.empty((1,rank))
    for i in range(rank):
        #print(Tgraph[1][i])
        x[0][i]=Tgraph[1][i]
    #print(x)
    
    
    
    y_pos = np.arange(len(Tgraph[0]))
    matplotlib.rcParams['font.family']=['SimHei']
    matplotlib.rcParams['font.sans-serif']=['SimHei']    
    plt.barh(y_pos,x[0][::-1],align='center',alpha=0.4)
    plt.yticks(y_pos, Tgraph[0][::-1])
    plt.xlabel('出现次数')   
    plt.title('词频条形图')  
    plt.show()  
   # for j in range(20):
    #    word,count = sortedList[j]
    #    print("{0:<10}{1:>5}".format(word,count))
finally:
    print("Finish!")
    #input()
    textFile.close()
