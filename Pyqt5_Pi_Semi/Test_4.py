import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个QLineEdit和一个QLabel
        self.lineEdit = QLineEdit(self)
        self.label = QLabel(self)
        self.label.setText("显示在文本框中输入的值")

        # 将LineEdit的文本变化信号与槽函数关联
        self.lineEdit.textChanged.connect(self.updateLabel)

        # 将控件添加到布局中
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label)

        # 设置布局
        self.setLayout(layout)

        # 设置窗口属性
        self.resize(100,100)
        self.setWindowTitle('LineEdit和Label示例')

    def updateLabel(self):
        # 获取LineEdit的文本并设置到Label上
        text = self.lineEdit.text()
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
