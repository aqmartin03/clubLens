import sqlite3

def create_tables():
    connection = sqlite3.connect("clublens.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rounds (
            id INTEGER PRIMARY KEY,
            date TEXT,
            course_name TEXT,
            score INTEGER
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shots (
            id INTEGER PRIMARY KEY,
            round_id INTEGER,
            hole INTEGER,
            club TEXT,
            starting_yardage REAL,
            starting_lie TEXT,
            ending_yardage REAL,
            ending_lie TEXT,
            miss_direction TEXT,
            miss_severity TEXT,
            penalty INTEGER,

            FOREIGN KEY (round_id) REFERENCES rounds(id)
        );
    """)
    connection.close()

def add_round(date, course_name):
    connection = sqlite3.connect("clublens.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO rounds (date, course_name) values (?, ?)",
        (date, course_name)
    )
    connection.commit()
    round_id = cursor.lastrowid
    connection.close()
    return round_id

def get_rounds():
    connection = sqlite3.connect("clublens.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM rounds"
    )
    rounds = cursor.fetchall()
    connection.close()
    return rounds

def add_shot(round_id, hole, club, starting_yardage, starting_lie, ending_yardage, ending_lie, miss_direction, miss_severity, penalty):
    connection = sqlite3.connect("clublens.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO shots (
            round_id, 
            hole, 
            club, 
            starting_yardage, 
            starting_lie, 
            ending_yardage, 
            ending_lie, 
            miss_direction, 
            miss_severity, 
            penalty
        ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            round_id, 
            hole, 
            club, 
            starting_yardage, 
            starting_lie, 
            ending_yardage, 
            ending_lie, 
            miss_direction, 
            miss_severity, 
            penalty
        )
    )
    connection.commit()
    connection.close()

def get_shots(round_id):
    connection = sqlite3.connect("clublens.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM shots WHERE round_id = ?",
        (round_id,)
    )
    shots = cursor.fetchall()
    connection.close()
    return shots