from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime

"""
can i suggest getting rid of the date widget in the log workouts, as can just use current time.
also confused about the goal widget stuff
also kind of want to get rid of the abstract class?
"""
# changed class names and changing stuff, lmk if it breaks something
# also getting rid of some of the raise stuff to stop errors if thats alright
# removing some of the validation just so we can get it up and running easier

# feel free to change anything here that affects you're task. This is just to get started.
# note the implementation of these methods is to be done by the database people,
# so any processing of data should be done before calling them - these methods are just for storing the data.


"""
needs validation eventually and more testing

how does the goal work?

what the db does rn 
    1. you have a user
    2. user starts a workout/session
    3. user logs exercises that they did in said session
    
    2. user logs bodyweight, separate from rest of program
    
added functions:
getBodyweightHistory      # bodyweight, bodyweight_date
getExerciseNameIdFromName # exercise_name_id
getExerciseInfo           # exercise_name_id, exercise_name, category
getAllSessionsByUserId    # session_id, user_id, session_date
getExerciseHistoryByName  # session_id, exercise_name_id, sets, reps, weight
logBodyweight
logExercise
createNewSession
removeUser
createUser
createDatabase  # removes all tables and creates new ones 

plus some more 
"""

class AbstractDatabase(ABC):
    # not actually sure what data about workouts is going to be logged.
    # maybe modify to store just an estimated 1rm rather than sets and reps?
    @abstractmethod
    def logExercise(self, exercise, sets, reps, weight):
        pass

    @abstractmethod
    def logBodyweight(self, weight):
        pass

    # return current bodyweight
    @abstractmethod
    def getBodyweight(self):
        pass

    # return array of (int time, int bodyweight)
    @abstractmethod
    def getBodyweightHistory(self):
        pass

    # return an array of tuples? e.g. (int time, int estimated_1rm) or (int time, int sets, int reps, float weight)
    @abstractmethod
    def getExerciseHistoryByName(self, exercise):
        pass

    # am assuming a Goal class will be made
    # @abstractmethod
    # def storeGoal(self, goal):
    #     pass
        # TODO srry dont know what this is meant to do, will comment out for now

    # have no idea how this is going to work, this will need to be changed.
    # method to update whether a goal has been met or not.

    # @abstractmethod
    # def updateGoal(self):
    #     pass

    # return array of goals
    # @abstractmethod
    # def getGoals(self):
    #     pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def setAge(self, age):
        pass

    @abstractmethod
    def setGender(self, gender):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAge(self):
        pass

    @abstractmethod
    def getGender(self, gender):
        pass

class Database(AbstractDatabase):
    def __init__(self, db_name="gymapp.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.user_id = 1 # change this and wherever this is used if we ever have multiple users

    def __del__(self):
        self.close()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None


    def _createDatabase(self):
        # Will delete all tables...
        self.cursor.execute("PRAGMA foreign_keys = OFF;")
        self.cursor.execute("DROP TABLE IF EXISTS bodyweight;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise_names;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise;")
        self.cursor.execute("DROP TABLE IF EXISTS sessions;")
        self.cursor.execute("DROP TABLE IF EXISTS users;")
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER DEFAULT 0,
                gender TEXT DEFAULT 'N/A'
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bodyweight (
                bodyweight_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                bodyweight REAL NOT NULL,
                bodyweight_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
        """)

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercise_names (
                exercise_name_id INTEGER PRIMARY KEY,
                exercise_name TEXT NOT NULL UNIQUE,
                category TEXT  
            );         
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                session_date DATETIME NOT NULL,
                duration FLOAT DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercise (
                exercise_id INTEGER PRIMARY KEY,
                session_id INTEGER,
                exercise_name_id INTEGER,
                sets INTEGER NOT NULL,
                reps INTEGER NOT NULL,
                weight INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
                FOREIGN KEY (exercise_name_id) REFERENCES exercise_names(exercise_name_id)
            );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals (
            goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        ''')


        # going to add in one default user
        # if we ever have multiple users,
        # remove this and update the functions
        self.createUser("main", "password", "email", 18, "MALE")
        self.conn.commit()

    def createUser(self, username, password, email, age=0, gender="N/A"):
        try:
            if not isinstance(username, str) or not username.strip():
                raise ValueError("Username must be a non-empty string.")
            if not isinstance(password, str) or not password.strip():
                raise ValueError("Password must be a non-empty string.")
            if not isinstance(email, str) or not email.strip():
                raise ValueError("Invalid email format.")
            self.cursor.execute("INSERT INTO users (username, password, email, age, gender) VALUES (?, ?, ?, ?, ?)", (username, password, email, age, gender))
            self.conn.commit()
        except ValueError as e:
            print(f"Error creating user: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None


    def removeUser(self, username):
        try:
            if not isinstance(username, str) or not username.strip():
                raise ValueError("Username must be a non-empty string.")
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.conn.commit()
        except ValueError as e:
            print(f"Error removing user: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def createNewSession(self, duration=None, user_id=None):
        print("Creating new session...")
        try:
            if user_id is None:
                user_id = self.user_id
            if not isinstance(duration, (int, float)) or duration < 0:
                duration = 0
            else:
                duration = float(duration)
            if not isinstance(user_id, int) or user_id < 1:
                raise ValueError("User ID must be a positive integer.")

            # Have to update last session with correct duratoin
            if duration is not None:


                self.cursor.execute("SELECT session_id FROM sessions WHERE user_id = ? ORDER BY session_date DESC LIMIT 1",
                    (user_id,))
                last_session = self.cursor.fetchone()
                if last_session:
                    self.cursor.execute(
                        "UPDATE sessions SET duration = ? WHERE session_id = ?",(duration, last_session[0]))

            self.cursor.execute("INSERT INTO sessions (user_id, session_date) VALUES (?, ?)", (user_id, datetime.now()))
            print("Updated previous session with duration")
            self.conn.commit()
        except ValueError as e:
            print(f"Error creating session: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"error: {e}")
            return None

    def getAllSessions(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        # session_id, user_id, session_date
        self.cursor.execute("SELECT * FROM sessions WHERE user_id = ? ORDER BY session_date DESC", (user_id,))
        return self.cursor.fetchall()

    def getExerciseInfo(self):
        # exercise_name_id, exercise_name, category
        self.cursor.execute("SELECT * FROM exercise_names")
        return self.cursor.fetchall()

    def _getExerciseNameIdFromName(self, exercise_name, category=None):
        # exercise_name_id, exercise_name, category
        try:
            if not isinstance(exercise_name, str) or not exercise_name.strip():
                raise ValueError("Exercise name must be a non-empty string.")
            exercise_name = exercise_name.upper()

            self.cursor.execute("SELECT exercise_name_id FROM exercise_names WHERE exercise_name = ?", (exercise_name,))
            result = self.cursor.fetchone()
            if result is None:
                print(f"Exercise '{exercise_name}' not found in database. Creating new entry.")
                self.cursor.execute("INSERT INTO exercise_names (exercise_name, category) VALUES (?, ?)", (exercise_name, category))
                self.conn.commit()
                self.cursor.execute("SELECT exercise_name_id FROM exercise_names WHERE exercise_name = ?", (exercise_name,))
                result = self.cursor.fetchone()
            return result[0]
        except ValueError as e:
            print(f"Error getting exercise name ID: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def logExercise(self, exercise_name, sets, reps, weight, user_id=None):
        # need to check that the info given is valid
        try:
            sets = int(sets)
            reps = int(reps)
            weight = float(weight)

            if user_id is None:
                user_id = self.user_id
            if not isinstance(exercise_name, str) or not exercise_name.strip():
                raise ValueError("Exercise name must be a non-empty string.")
            if not isinstance(sets, int) or sets <= 0:
                raise ValueError("Sets must be a positive integer.")
            if not isinstance(reps, int) or reps <= 0:
                raise ValueError("Reps must be a positive integer.")
            if not isinstance(weight, (int, float)) or weight < 0:
                raise ValueError("Weight must be a non-negative number.")

            last_session_id = self.getAllSessions(user_id)[0][0]
            if last_session_id is None:
                raise ValueError("no session found for given user")
            # TODO one option is to start a new session atp
            exercise_name_id = self._getExerciseNameIdFromName(exercise_name.upper())
            print(exercise_name_id, sets, reps, weight)
            self.cursor.execute("INSERT INTO exercise (session_id, exercise_name_id, sets, reps, weight) VALUES (?, ?, ?, ?, ?)", (last_session_id, exercise_name_id, sets, reps, weight))
            self.conn.commit()
            return True
        except ValueError as e:
            print(f"Error logging exercise: {e}")
            return False
        except IndexError as e:
            print(f"Error: {e}. No sessions found for user ID {user_id}.Creating new session and will try again")
            self.createNewSession(user_id)
            self.logExercise(exercise_name, sets, reps, weight, user_id)


        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def logBodyweight(self, weight, user_id=None):
        try:
            if user_id is None:
                user_id = self.user_id
            if not isinstance(weight, (int, float)) or weight <= 0:
                raise ValueError("Weight must be a positive number.")
            self.cursor.execute("INSERT INTO bodyweight (user_id, bodyweight, bodyweight_date) VALUES (?, ?, ?)", (user_id, weight, datetime.now()))
            self.conn.commit()
        except ValueError as e:
            print(f"Error logging bodyweight: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def getBodyweightHistory(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        # bodyweight, bodyweight_date
        self.cursor.execute("SELECT bodyweight, bodyweight_date FROM bodyweight WHERE user_id = ? ORDER BY bodyweight_date ASC", (user_id,)) # changed desc to asc - hope this doesnt mess anything up
        return self.cursor.fetchall()

    def getExerciseHistoryByName(self, exercise_name, user_id=None):
        if user_id is None:
            user_id = self.user_id
        exercise_name = exercise_name.upper()
        exercise_name_id = self._getExerciseNameIdFromName(exercise_name)
        # session_id, exercise_name_id, sets, reps, weight
        self.cursor.execute("SELECT exercise_name_id, sets, reps, weight FROM exercise WHERE exercise_name_id = ? AND session_id IN (SELECT session_id FROM sessions WHERE user_id = ?) ORDER BY session_id", (exercise_name_id, user_id))
        return self.cursor.fetchall()

    def getGender(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        self.cursor.execute("SELECT gender FROM users WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def getAge(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        self.cursor.execute("SELECT age FROM users WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def setName(self, name, user_id=None):
        try:
            if user_id is None:
                user_id = self.user_id
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name must be a non-empty string.")
            self.cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", (name, user_id))
            self.conn.commit()
        except ValueError as e:
            print(f"Error setting name: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None


    def setAge(self, age, user_id=None):
        try:
            if user_id is None:
                user_id = self.user_id
            if not isinstance(age, int) or age < 0:
                raise ValueError("Age must be a non-negative integer.")
            self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id))
            self.conn.commit()
        except ValueError as e:
            print(f"Error setting age: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None


    def getBodyweight(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        self.cursor.execute("SELECT bodyweight FROM bodyweight WHERE user_id = ? ORDER BY bodyweight_date DESC LIMIT 1", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def getName(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        self.cursor.execute("SELECT username FROM users WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None


    def setGender(self, gender, user_id=None):
        if user_id is None:
            user_id = self.user_id
        try:
            if user_id is None:
                user_id = self.user_id
            if not isinstance(gender, str):
                raise ValueError("Gender must be a string.")
            self.cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id))
            self.conn.commit()
        except ValueError as e:
            print(f"Error setting age: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def createNewExercise(self, exercise_name, category=None):
        try:
            if not isinstance(exercise_name, str) or not exercise_name.strip():
                raise ValueError("Exercise name must be a non-empty string.")
            exercise_name = exercise_name.upper()
            self.cursor.execute("INSERT INTO exercise_names (exercise_name, category) VALUES (?, ?)", (exercise_name, category))
            self.conn.commit()
        except ValueError as e:
            print(f"Error creating exercise: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def removeLastSession(self):
        try:
            last_session = self.getAllSessions()[0]
            session_id = last_session[0]
            self.cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            self.conn.commit()
        except IndexError as e:
            print(f"Error: {e}. No sessions found.")
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def getGoals(self):
        self.cursor.execute("SELECT name FROM goals")
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def addGoal(self, string):
        string = str(string)  # just to be safe
        self.cursor.execute("INSERT INTO goals (name) VALUES (?)", (string,))
        self.conn.commit()



    def removeGoal(self, string):
        try: # lazy
            string = str(string)
            self.cursor.execute("DELETE FROM goals WHERE name = ?", (string,))
            self.conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            return None















def tests():
    # running tests
    db = Database()

    # Uncomment this to create a fresh database
    # db._createDatabase()

    db.cursor.execute("SELECT * FROM users")
    print(db.cursor.fetchall())

    # db.logBodyweight(80)
    # db.logBodyweight(81)
    # db.logBodyweight(82)

    db.createNewExercise("deadlift", "lower")
    db.createNewExercise("bench press", "upper")
    db.createNewExercise("squats", "lower")
    db.createNewExercise("pull ups", "upper")
    db.createNewExercise("leg press", "lower")
    db.createNewExercise("overhead press", "upper")
    db.createNewExercise("lat pulldowns", "upper")
    db.createNewExercise("leg extensions", "lower")
    db.createNewExercise("leg curls", "lower")
    db.createNewExercise("lateral raises", "upper")
    db.createNewExercise("bicep curls", "upper")

    #
    # db.logExercise("bench", 3, 5, 10)
    #
    # db.logExercise("squat", 3, 5, 20)
    # db.logExercise("squat", 3, 5, 30)
    # db.logExercise("deadlift", 3, 5, 30)
    #
    # db.createNewSession()
    # db.logExercise("bench", 3, 5, 40)
    # db.logExercise("squat", 3, 5, 50)
    # db.logExercise("deadlift", 3, 5, 60)
    # db.logExercise("deadlift", 3, 5, 70)



    print(db.getExerciseHistoryByName("bench"))
    print(db.getExerciseHistoryByName("will this error"))
    print(db.getBodyweight())
    print(db.getBodyweightHistory())
    print(db.getExerciseInfo())
    print(db.getExerciseHistoryByName("deadlift"))

    db.cursor.execute("SELECT * FROM users")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM bodyweight")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM exercise_names")
    print(db.cursor.fetchall())
    print("sessions")
    db.cursor.execute("SELECT * FROM sessions")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM exercise")
    print(db.cursor.fetchall())



if __name__ == "__main__":
    tests()
