import sys
import functools

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greetings(who):
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f'Hello, {who}!')


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Signals and slots")

layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(functools.partial(greetings, "World"))

layout.addWidget(button)

msg = QLabel("")
msg.setAlignment(Qt.AlignCenter)

layout.addWidget(msg)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())