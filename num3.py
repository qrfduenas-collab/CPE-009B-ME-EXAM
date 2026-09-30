import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

def display_fullname():
    entry2.setText(entry1.text())

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Midterm in OOP")
window.setGeometry(400, 200, 500, 280)

label = QLabel("Enter your fullname:", window)
label.setGeometry(50, 60, 150, 30)
label.setStyleSheet("color: red;")

entry1 = QLineEdit(window)
entry1.setGeometry(210, 55, 220, 35)

button = QPushButton("Click to display your Fullname", window)
button.setGeometry(50, 120, 155, 35)
button.setStyleSheet("color: red;")

entry2 = QLineEdit(window)
entry2.setGeometry(210, 120, 220, 35)

button.clicked.connect(display_fullname)

window.show()

sys.exit(app.exec())