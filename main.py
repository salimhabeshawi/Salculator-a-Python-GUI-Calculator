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
        self.resize(400, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #232946;
            }
        """)

        # All App Objects
        self.text_box = QLineEdit()
        self.text_box.setStyleSheet(
            """
            QLineEdit {
                background: #121629;
                color: #eebbc3;
                border: none;
                border-radius: 12px;
                padding: 18px;
                font-size: 32px;
                font-family: 'Segoe UI', 'Helvetica Neue', Arial, 'Liberation Sans', sans-serif;
                margin-bottom: 18px;
            }
            """
        )
        self.text_box.setFont(QFont("Segoe UI", 32))
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
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: #eebbc3;
                    color: #232946;
                    border: none;
                    border-radius: 12px;
                    font: 20pt 'Segoe UI', 'Helvetica Neue', Arial, 'Liberation Sans', sans-serif;
                    padding: 18px;
                    margin: 6px;
                    min-width: 60px;
                    min-height: 60px;
                    transition: background 0.2s;
                }}
                QPushButton:hover {{
                    background-color: #f6c9c9;
                }}
                QPushButton:pressed {{
                    background-color: #b8c1ec;
                }}
            """)
            self.main_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("C")
        self.back = QPushButton("del")
        for btn in [self.clear, self.back]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #b8c1ec;
                    color: #232946;
                    border: none;
                    border-radius: 12px;
                    font: 18pt 'Segoe UI', 'Helvetica Neue', Arial, 'Liberation Sans', sans-serif;
                    padding: 16px 0;
                    margin: 6px;
                    min-width: 60px;
                    min-height: 50px;
                    transition: background 0.2s;
                }
                QPushButton:hover {
                    background-color: #eebbc3;
                }
                QPushButton:pressed {
                    background-color: #232946;
                    color: #eebbc3;
                }
            """)

        # All Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.main_grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.back)
        button_row.setSpacing(16)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(24, 24, 24, 24)
        master_layout.setSpacing(18)

        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.back.clicked.connect(self.button_click)
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
    # No need to set global stylesheet here, handled in widget styles
    main_window.show()
    app.exec_()
