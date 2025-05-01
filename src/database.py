import sqlite3

class Database:
    def __init__(self, db_name = "data.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self): # function to create table

        CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
                                userId INTEGER PRIMARY KEY AUTOINCREMENT,
                                fullName TEXT NOT NULL,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL
                                );
                            """

        CREATE_TASK_TABLE = """ CREATE TABLE IF NOT EXISTS tasks (
                                taskId INTEGER PRIMARY KEY AUTOINCREMENT,
                                taskName TEXT NOT NULL,
                                courseName TEXT NOT NULL,
                                priority TEXT NOT NULL,
                                due DATE NOT NULL
                                );"""
        
        connection = self.connect()
        with connection:
            connection.execute(CREATE_TASK_TABLE)
            connection.execute(CREATE_USER_TABLE)
        connection.close()


    def insert_info(self, taskName, courseName, priority, due): # Function to insert tasks to the task table

        INSERT_TASKS =  """ INSERT INTO tasks (
                            taskName, 
                            courseName,
                            priority,
                            due)
                            values (?, ?, ?, ?);
                            """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_TASKS, (taskName, courseName, priority, due))
        connection.close()

    def create_user(self, fullName ,userName, password):

        INSERT_USER = """ INSERT INTO users (
                            fullName,
                            email,
                            password)
                            values(?, ?, ?);
                            """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_USER, (fullName, userName, password))
        connection.close()
            
    def user_log_in(self, email, password):
        INFO = """SELECT * FROM users WHERE email = ? AND password = ?"""
        connection = self.connect
        with connection:
            cursor = connection.execute(INFO, (email, password))
            user = cursor.fetchone()
        connection.close()
        return user