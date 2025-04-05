import sqlite3

class Database:
    def __init__(self, db_name = "data.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self): # function to create "task" table

        CREATE_TASK_TABLE = """ CREATE TABLE IF NOT EXISTS tasks (
                                taskId INTEGER AUTO INCREMENT PRIMARY KEY,
                                taskName TEXT NOT NULL,
                                courseName TEXT NOT NULL,
                                priority TEXT NOT NULL,
                                due DATE NOT NULL
                                );"""
        
        connection = self.connect()
        with connection:
            connection.execute(CREATE_TASK_TABLE)
        connection.close()


    def insert_info(self, taskName, courseName, priority): # Function to insert tasks to the task table

        INSERT_TASKS =  """ INSERT INTO tasks (
                            taskName, 
                            courseName,
                            priority,
                            due)
                            values (?, ?, ?, ?);
                            """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_TASKS, (taskName, courseName, priority))
        connection.close()
            