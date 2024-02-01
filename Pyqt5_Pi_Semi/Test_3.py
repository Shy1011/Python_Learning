import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("0", self)
        layout.addWidget(self.label)

        self.btn = QPushButton("Increment", self)
        self.btn.clicked.connect(self.incrementCounter)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def incrementCounter(self):
        current_value = int(self.label.text())
        new_value = current_value + 1
        self.label.setText(str(new_value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    counter_app = CounterApp()
    counter_app.show()
    sys.exit(app.exec_())
