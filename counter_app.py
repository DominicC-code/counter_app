import random
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Clicker Counter")
        self.label = QLabel()
        self.highscore_label = QLabel()
        self.highscore_value = 0
        self.click = QPushButton("Click Me!")
        self.counter = 0
        self.reset = QPushButton("Reset")
        try:
            with open("highscore.txt", "r") as file:
                self.highscore_value = int(file.read())
        except:
            self.highscore_value = 0
        self.initUI()

        self.click.clicked.connect(self.add_click)
        self.reset.clicked.connect(self.reset1)

    def add_click(self):
        self.counter += 1
        self.label.setText(str(self.counter))

        if self.counter > self.highscore_value:
            self.highscore_value = self.counter
            self.highscore_label.setText(f"High Score: {self.highscore_value}")

            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore_value))

    def reset1(self):
        self.counter = 0
        self.label.setText(str(self.counter))

    def initUI(self):
        self.highscore_label.setText(f"High Score: {self.highscore_value}")
        vbox = QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addWidget(self.click)
        vbox.addWidget(self.reset)
        vbox.addWidget(self.highscore_label)
        self.setLayout(vbox)

        self.setStyleSheet("""
        QLabel{
            background-color: rgb(200, 200, 200);
            font-size: 100px
        }
        QPushButton{
            font-size: 30px;
            background-color: blue;
        }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = mainWindow()
    main_window.show()
    sys.exit(app.exec())