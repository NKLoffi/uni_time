import sqlite3
import bcrypt

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
                                userId INTEGER NOT NULL,
                                courseName TEXT NOT NULL,
                                assignment TEXT NOT NULL,
                                description TEXT NOT NULL,
                                due DATE NOT NULL,
                                FOREIGN KEY (userId) REFERENCES users(userId)
                                );"""
        
        CREATE_JOB_TABLE = """CREATE TABLE IF NOT EXISTS jobs (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              jobId TEXT NOT NULL,
                              userId INTEGER NOT NULL,
                              jobTitle TEXT NOT NULL,
                              company TEXT NOT NULL,
                              appliedDate DATE NOT NULL,
                              notes TEXT NOT NULL,
                              status TEXT NOT NULL,
                              FOREIGN KEY (userId) REFERENCES users(userId)
                              );"""
        
        connection = self.connect()
        with connection:
            # connection.execute("DROP TABLE IF EXISTS jobs;")
            connection.execute(CREATE_TASK_TABLE)
            connection.execute(CREATE_USER_TABLE)
            connection.execute(CREATE_JOB_TABLE)
        connection.close()



    
    def create_jobs(self, userId, jobId, jTitle, company, aDate, notes, status):

        INSERT_JOBS = """ INSERT INTO jobs (
                          jobId,
                          userId,
                          jobTitle,
                          company,
                          appliedDate,
                          notes,
                          status)
                          values(?, ?, ?, ?, ?, ?, ?);
                    """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_JOBS, (jobId, userId, jTitle, company, aDate, notes, status))
        connection.close()

    def get_jobs(self, userId):                                                          # Function to fetch jobs from the database
        JOBS = """SELECT jobId, jobTitle, company, appliedDate, notes, status FROM jobs WHERE userId = ?"""
        connection = self.connect()
        with connection:
            cursor = connection.execute(JOBS, (userId,))
            jobs = cursor.fetchall()
        connection.close()
        return jobs

    def insert_info(self, userId, courseName, assignment, description, due): # Function to insert tasks to the task table

        INSERT_TASKS =  """ INSERT INTO tasks ( 
                            userId,
                            courseName,
                            assignment,
                            description,
                            due)
                            values (?, ?, ?, ?, ?);
                            """
        
        connection = self.connect()
        with connection:
            connection.execute(INSERT_TASKS, (userId, courseName, assignment, description, due))
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
            
    def user_log_in(self, email, entered_password):
        INFO = """SELECT userId, fullName, email, password FROM users WHERE email = ?"""
        connection = self.connect()
        with connection:
            cursor = connection.execute(INFO, (email,))
            result = cursor.fetchone()
        connection.close()

        if result:
            userId, fullName, email, hashed_password = result
            if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
                return (userId, fullName, email)
        return None
    
    def get_tasks(self, userId):
        TASK = """SELECT taskId, courseName, assignment, description, due FROM tasks WHERE userId = ?"""
        connection = self.connect()
        with connection:
            cursor = connection.execute(TASK, (userId,) )
            tasks = cursor.fetchall()
        connection.close()
        return tasks

    def dlt_task(self, taskId):

        DLT = """DELETE FROM tasks WHERE taskId = ?"""

        connection = self.connect()
        with connection:
            connection.execute(DLT, (taskId,))
        connection.close()

    def update_job_status(self, job_id, status):
        UPDATE_STATUS = "UPDATE jobs SET status = ? WHERE jobId = ?"
        connection = self.connect()
        with connection:
            connection.execute(UPDATE_STATUS, (status, job_id))
        connection.close()

    def dlt_job(self, jobId):

        DLT = """DELETE FROM jobs WHERE jobId = ?"""

        connection = self.connect()
        with connection:
            connection.execute(DLT, (jobId,))
        connection.close()
