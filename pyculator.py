#!/usr/bin/env python3

import sys
import functools

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

ERROR_MESSAGE = "ERROR"

class PyculatorUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyculator")
        self.setFixedSize(335, 270)

        self.generalLayout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)

        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttons = {}

        buttonsLayout = QGridLayout()

        buttonsDict = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }

        for buttonText, buttonPosition in buttonsDict.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(60, 40)

            buttonsLayout.addWidget(self.buttons[buttonText], buttonPosition[0], buttonPosition[1])

        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
    
    def displayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.setDisplayText("")


class PyculatorControl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectSignals()
    
    def _connectSignals(self):
        for buttonText, button in self._view.buttons.items():
            if buttonText not in {"=", "C"}:
                button.clicked.connect(functools.partial(self._buildExpression, buttonText))
        
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
    
    def _buildExpression(self, expression):
        if self._view.displayText() == ERROR_MESSAGE:
            self._view.clearDisplay()

        newExpression = self._view.displayText() + expression
        self._view.setDisplayText(newExpression)
    
    def _calculateResult(self):
        result = self._model(self._view.displayText())
        self._view.setDisplayText(result)


def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MESSAGE
    
    return result


def main():
    pyculator = QApplication(sys.argv)

    view = PyculatorUi()
    view.show()

    controller = PyculatorControl(evaluateExpression, view)

    sys.exit(pyculator.exec_())


if __name__ == "__main__":
    main()