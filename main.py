# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QGridLayout,
)
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App Objects and Settings
        self.setWindowTitle("Salculator")
        self.resize(800, 1000)

        # All App Objects
        self.text_box = QLineEdit()
        self.text_box.setStyleSheet(
            """
            padding: 10px;
            """
        )
        self.text_box.setFont(QFont("Helvetica", 32))
        self.main_grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
        ]

        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet(
                """
                QPushButton {
                    font: 25pt Comic Sans MS;
                    padding: 10px;
                }
                """
            )
            self.main_grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("C")
        self.back = QPushButton("del")

        # All Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.main_grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.back)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)

        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.back.clicked.connect(self.button_click)
        self.clear.setStyleSheet(
            """
            QPushButton {
                font: 25pt Comic Sans MS;
                padding: 10px;
            }
            """
        )
        self.back.setStyleSheet(
            """
            QPushButton {
                font: 25pt Comic Sans MS;
                padding: 10px;
            }
            """
        )
    # Functions
    def button_click(self):
        btn = self.sender()
        txt = btn.text()

        if txt == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))

            except Exception as e:
                print("Error: ", e)

        elif txt == "C":
            self.text_box.clear()

        elif txt == "del":
            concurrent_text = self.text_box.text()
            self.text_box.setText(concurrent_text[:-1])

        else:
            concurrent_text = self.text_box.text()
            self.text_box.setText(concurrent_text + txt)


# Show/Run App
if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet(
        """
        QWidget {
            background-color: #bcb4d5
        }
        """
    )
    main_window.show()
    app.exec_()