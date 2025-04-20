from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

def create_settings_page(main_window):
    page = QWidget()
    layout = QVBoxLayout()

    top_bar = QHBoxLayout()
    back_btn = main_window.create_back_button(None, main_window.welcomePage)
    back_btn.setObjectName("settings_back")
    top_bar.addWidget(back_btn)
    top_bar.addStretch()

    layout.addLayout(top_bar)
    layout.addWidget(QLabel("Settings Page"))

    page.setLayout(layout)
    return page
