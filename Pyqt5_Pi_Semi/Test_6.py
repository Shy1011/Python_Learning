from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Centered Text Button")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        button = QPushButton("Click me")
        button.setStyleSheet("text-align: left;")  # 设置文本水平居中
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
