import sqlite3


def executedb(sqliteCommand):
    try:
        sqLiteConnection = sqlite3.connect("links.sqlite")
        cursor = sqLiteConnection.cursor()
        sqliteCommand = sqliteCommand
        cursor.execute(sqliteCommand)
        sqLiteConnection.commit()
        record = cursor.fetchall()
        print(record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqLiteConnection:
            sqLiteConnection.close()
            print("sqLiteConnection closed")
