import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QDialog")

        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())

        dialogLayout.addLayout(formLayout)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = Dialog()
    dialog.show()

    sys.exit(dialog.exec_())