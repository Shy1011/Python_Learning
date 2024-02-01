import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.stackedWidget = QStackedWidget(self)

        self.page1 = QWidget()
        self.page1Button = QPushButton('Switch to Page 2', self.page1)
        self.page1Label = QLabel('Page 1', self.page1)

        self.page1Layout = QVBoxLayout(self.page1)
        self.page1Layout.addWidget(self.page1Button)
        self.page1Layout.addWidget(self.page1Label)

        self.page2 = QWidget()
        self.page2Button = QPushButton('Switch to Page 1', self.page2)
        self.page2Label = QLabel('Page 2', self.page2)

        self.page2Layout = QVBoxLayout(self.page2)
        self.page2Layout.addWidget(self.page2Button)
        self.page2Layout.addWidget(self.page2Label)

        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)

        layout.addWidget(self.stackedWidget)

        self.page1Button.clicked.connect(self.switchToPage2)
        self.page2Button.clicked.connect(self.switchToPage1)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Page Switching Example')

    def switchToPage2(self):
        self.stackedWidget.setCurrentIndex(1)

    def switchToPage1(self):
        self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
