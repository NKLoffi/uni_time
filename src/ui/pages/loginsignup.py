from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt 

def loginsignup(main_window):

    page = QWidget()
    layout = QVBoxLayout()

    top_bar = QHBoxLayout()
    back_btn = main_window.create_back_button(None, main_window.welcomePage)
    back_btn.setObjectName("settings_back")
    top_bar.addWidget(back_btn)
    top_bar.addStretch()

    btn_layout = QVBoxLayout()
    btn_layout.setSpacing(5)
    login_btn = QPushButton("Login")
    login_btn.setObjectName("l_btn")
    signup_btn = QPushButton("Sign Up")
    signup_btn.setObjectName("s_btn")

    btn_layout.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
    btn_layout.addWidget(signup_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

    layout.addLayout(btn_layout)
    layout.addLayout(top_bar)

    page.setLayout(layout)
    return page