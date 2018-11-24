#GUI
import sys,os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
def show_name():
    name = nameLine.text()
    if name == "":
        QMessageBox.information(nameLine,"输入为空","请输入姓名")
        return
    else:
        QMessageBox.information(nameLine,"Well Done!",\
                                "Hello {}!".format(name))
app = QApplication(sys.argv)
mywidget = QWidget()
nameLabel = QLabel("姓名：")
nameLine = QLineEdit(mywidget)
EnterButton = QPushButton("Enter",mywidget)

subLayout = QHBoxLayout()
subLayout.addStretch(1)
subLayout.addWidget(EnterButton)
bodyLayout = QVBoxLayout()
bodyLayout.addWidget(nameLabel)
bodyLayout.addWidget(nameLine)
bodyLayout.addLayout(subLayout)

EnterButton.clicked.connect(show_name)
mywidget.setLayout(bodyLayout)
#mywidget.setGeometry(200,200,600,300)#x,y,width,height
mywidget.setWindowTitle('Hello PyQt')
#screen = QDesktopWidget().screenGeometry()
#size = mywidget.geometry()
#qtn.move((size.width()-qtn.sizeHint().width())/2,size.height()*4/5)
#mywidget.move((screen.width()-size.width())/2,\
#                (screen.height()-size.height())/2)
mywidget.show()
sys.exit(app.exec_())
