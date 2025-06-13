WINDOW_STYLES = """

                QMainWindow{
                background-color: hsl(40, 3%, 20%);
                }

                QTableView{
                background-color: hsl(41, 3%, 20%);
                gridline-color:white;
                color: white;
                border: 1px solid black;
                }

                QHeaderView::section {
                background-color: hsl(41, 3%, 25%) !important;
                color: white;
                border: 1px solid black;
                }

                QAbstractScrollArea {
                    background-color: hsl(41, 3%, 20%);
                }

                QTableCornerButton::section {
                background-color: hsl(41, 3%, 25%) !important;
                border: 1px solid black;
                }


                QLabel#mainLabel,
                QLabel#label_4,
                QLabel#label_3{
                color: white;
                font-weight: bold;
                font-size: 30px;
                text-align: center;
                }

                QLabel#notesLabel,
                QLabel#DescriptionLabel,
                QLabel#jIdLabel,
                QLabel#jTitleLabel,
                QLabel#DueLabel,
                QLabel#AssignmentLabel,
                QLabel#courseLabel,
                QLabel#userLabel,
                QLabel#passLabel,
                QLabel#nameLabel,
                QLabel#emailLabel,
                QLabel#passLabel,
                QLabel#cPassLabel,
                QLabel#aDateLabel{
                color: white;
                }

                QLabel#loginLabel{
                color: white;
                font-weight: bold;
                font-size: 23px;
                text-align: center;
                }

                QLabel#label{
                color: white;
                font-weight: bold;
                font-size: 23px;
                text-align: center;
                padding: 25px;
                }

                QPushButton#backButton,
                QPushButton#backbtn,
                QPushButton#deleteButton,
                QPushButton#logOutButton{
                background-color: transparent;
                border: none;
                }
 
                QPushButton#started{
                background-color: hsl(217, 72%, 35%);
                color: white;
                min-width: 150px;
                max-width: 150px;
                min-height: 25px;
                max-height: 25px;
                border-radius: 5px;
                }

                QPushButton#jobBtn,
                QPushButton#docbtn,
                QPushButton#pushButton{
                background-color: hsl(217, 72%, 35%);
                color: white;
                border-radius: 5px;
                min-width: 100px;
                max-width: 100px;
                min-height: 25px;
                max-height: 25px;
                }

                QPushButton#jobBtn:hover,
                QPushButton#docbtn:hover,
                QPushButton#pushButton:hover{
                background-color: hsl(200, 72%, 35%);
                }

                QPushButton#createAccButton:hover,
                QPushButton#loginButton:hover,
                QPushButton#signupButton:hover,
                QPushButton#addButton:hover{
                background-color: hsl(200, 72%, 35%);
                }

                QPushButton#cacc{
                background-color: hsl(217, 67%, 44%);
                color: white;
                min-width: 150px;
                max-width: 150px;
                min-height: 25px;
                max-height: 25px;
                border-radius: 5px;
                }

                QPushButton#l_btn{
                background-color: hsl(217, 67%, 44%);
                color: white;
                min-width: 150px;
                max-width: 150px;
                min-height: 25px;
                max-height: 25px;
                border-radius: 5px;
                }

                QPushButton#createAccButton,
                QPushButton#loginButton,
                QPushButton#signupButton,
                QPushButton#addButton{
                background-color: hsl(217, 67%, 44%);
                color: white;
                min-width: 150px;
                max-width: 150px;
                min-height: 25px;
                max-height: 25px;
                border-radius: 5px;
                }

                QLineEdit{
                background-color: hsl(40, 3%, 37%);
                border: solid black;
                border-radius: 5px;
                margin-left: 10px;
                min-width: 300px;
                max-width: 400px;
                min-height: 25px;
                max-height: 25px;
                color: white;
                }


                QComboBox {
                background-color: hsl(40, 3%, 25%);
                padding: 4px 8px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-size: 13px;
                color: white;
                }

                QComboBox QAbstractItemView {
                background-color: hsl(40, 3%, 50%);
                selection-background-color: hsl(40, 3%, 50%);
                selection-color: hsl(40, 3%, 70%);
                color: white;
                }

                QDateEdit{
                background-color: hsl(40, 3%, 37%);
                border-radius: 5px;
                color: white;
                border: 1px solid black;
                }

                QCheckBox::indicator:unchecked {
                background-color: hsl(40, 3%, 37%);
                border-radius: 5px;
                border: 0.5px solid #ccc;
                }
                

                """