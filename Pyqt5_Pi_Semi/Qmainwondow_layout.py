from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

"""
在Qt中，`QMainWindow`是一个特殊的窗口类，通常用于应用程序的主窗口。`QMainWindow`提供了一种结构，
可以容纳工具栏、菜单栏、状态栏等，以及一个<font color="#f79646">中心区域</font>，用于放置主要的应用程序窗口部件（widget）。
`QMainWindow`并没有像`QWidget`一样直接提供布局管理器（layout manager）的支持，因为它的设计目的是为了更灵活地适应各种应用程序布局需求。

"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)  # 将中心部件设置为Qwidget 不能直接在mainwinodw中设置布局,但是可以在widget中设置布局

        layout = QVBoxLayout()
        # layout = QVBoxLayout(central_widget) # 这个也是将layout布局传递到widget中

        button1 = QPushButton('Button 1', central_widget)
        button2 = QPushButton('Button 2', central_widget)

        layout.addWidget(button1)
        layout.addWidget(button2)

        central_widget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
