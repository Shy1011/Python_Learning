
"""
怎样使用label做状态栏

槽函数的参数怎么使用第一次在这里产生了疑问

"""
from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    i = 0
    def __init__(self):
        super().__init__()

        # 创建 QLineEdit
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type something...")

        self.label = QLabel()
        self.btn = QPushButton()
        self.btn.setText("Add")

        # 创建布局，将 QLineEdit 添加到布局中
        layout = QVBoxLayout()
        # layout.addWidget(self.line_edit)
        layout.addWidget(self.label)
        layout.addWidget(self.btn)

        # 设置主窗口布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 连接 QLineEdit 的 textChanged 信号到槽函数
        self.line_edit.textChanged.connect(self.on_line_edit_text_changed)
        self.btn.clicked.connect(self.on_line_edit_text_changed)

    def on_line_edit_text_changed(self, text):
        self.i = self.i + 1
        self.line_edit.setText("")
        print(f"LineEdit Text Changed: {text}")
        self.label.setText(str(self.i))

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
