'''

创建和使用菜单

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow) :
    def __init__(self):
        super(Menu,self).__init__()
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction("新建")   # 这是一种方式

        save = QAction("保存",self)  # 这是另一种方式,而且这种方式可以添加动作
        save.setShortcut("Ctrl + S") # 为这个选项添加快捷键
        file.addAction(save) #  把save按键加到文件选项卡里去
        # file.addAction("Save")

        save.triggered.connect(self.process)

        edit = bar.addMenu("Edit") # 1
        edit.addAction("copy") # 2
        # copy.triggered.connect(self.process)
        edit.addAction("paste") # 2
        quit = QAction("退出",self) # 这是另一种
        edit.addAction(quit)

    def process(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())