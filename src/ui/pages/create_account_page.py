from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

def create_account_page(main_window):
    page = QWidget()
    layout = QVBoxLayout()

    top_bar = QHBoxLayout()
    back_btn = main_window.create_back_button(None, main_window.welcomePage)
    back_btn.setObjectName("back")
    top_bar.addWidget(back_btn)
    top_bar.addStretch()
    top_bar.addWidget(main_window.create_settings_button())
    layout.addLayout(top_bar)

    fields = {
        "Full Name": "eg. John",
        "DOB": "eg. DD-MM-YYYY",
        "Email": "jdoe@gmail.com",
        "Password": "Enter a password",
        "Confirm Password": "Confirm your password"
    }

    for label_text, placeholder in fields.items():
        label = QLabel(label_text)
        textbox = QLineEdit()
        textbox.setPlaceholderText(placeholder)
        textbox.setMinimumWidth(200)
        textbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
        layout.addWidget(textbox)

    layout.addWidget(QLabel("second page", alignment=Qt.AlignmentFlag.AlignCenter))
    page.setLayout(layout)
    return page