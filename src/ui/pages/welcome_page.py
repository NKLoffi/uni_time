from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

def create_welcome_page(main_window):
    page = QWidget()
    layout = QVBoxLayout()

    top_bar = QHBoxLayout()
    top_bar.addStretch()
    top_bar.addWidget(main_window.create_settings_button())
    layout.addLayout(top_bar)

    introLabel = QLabel("Welcome to Uni Time")
    introSubLabel = QLabel("Productivity is the key")
    introLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    introSubLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout.addStretch()
    layout.addWidget(introLabel)
    layout.addWidget(introSubLabel)

    getStartedButton = QPushButton("Get Started")
    getStartedButton.setObjectName("started")
    getStartedButton.clicked.connect(lambda: main_window.stack.setCurrentWidget(main_window.createAccountPage))

    button_layout = QHBoxLayout()
    button_layout.addStretch()
    button_layout.addWidget(getStartedButton)
    button_layout.addStretch()

    layout.addLayout(button_layout)
    layout.addStretch()
    layout.setSpacing(4)

    page.setLayout(layout)
    return page