import mysql.connector
from datetime import datetime


def insert_into_database(person_count: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="home"
    )

    cursor = db.cursor()

    current_datetime = datetime.now()

    sql = "insert into person_count (timestamp, count) VALUES (%s, %s)"

    cursor.execute(sql, (current_datetime, person_count))
    db.commit()
    cursor.close()
    db.close()

    print("\nData inserted successfully\n")
