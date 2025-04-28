import sqlite3

class Database:
    def __init__(self, db_name = "data.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self): # function to create table

        CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
                                userId INTEGER PRIMARY KEY AUTOINCREMENT,
                                userName TEXT NOT NULL,
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

    def create_user(self, userName, password):

        INSERT_USER = """ INSERT INTO users (
                            userName,
                            password)
                            values(?, ?);
                            """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_USER, (userName, password))
        connection.close()
            