#GUI wordCount
import sys,os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import jieba
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib

def getFileName():
    fileName = textLine.text()
    rank = eval(rankLine.text())
    try:
        textFile = open(fileName,"rt")
    except FileNotFoundError:
        QMessageBox.information(textLine,"打开错误","无法打开指定文件！")
        return
    else:
        wordCount(textFile,rank)
        textFile.close()

def wordCount(textFile,rank = 10):
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

    #rank = 10
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
    
app = QApplication(sys.argv)
mywidget = QWidget()
textLabel1 = QLabel("请输入要处理的文件名：")
textLine = QLineEdit(mywidget)
textLabel2 = QLabel("请输入要查看的词条数目：")
rankLine = QLineEdit(mywidget)
EnterButton = QPushButton("确定",mywidget)

subLayout = QHBoxLayout()
subLayout.addStretch(1)
subLayout.addWidget(EnterButton)
bodyLayout = QVBoxLayout()
bodyLayout.addWidget(textLabel1)
bodyLayout.addWidget(textLine)
bodyLayout.addWidget(textLabel2)
bodyLayout.addWidget(rankLine)
bodyLayout.addLayout(subLayout)

EnterButton.clicked.connect(getFileName)
mywidget.setLayout(bodyLayout)
#mywidget.setGeometry(200,200,600,300)#x,y,width,height
mywidget.setWindowTitle('文件词频统计器')
#screen = QDesktopWidget().screenGeometry()
#size = mywidget.geometry()
#qtn.move((size.width()-qtn.sizeHint().width())/2,size.height()*4/5)
#mywidget.move((screen.width()-size.width())/2,\
#                (screen.height()-size.height())/2)
mywidget.show()
sys.exit(app.exec_())
