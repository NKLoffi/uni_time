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
                QLabel#label_3{
                color: white;
                font-weight: bold;
                font-size: 30px;
                text-align: center;
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
                
                """