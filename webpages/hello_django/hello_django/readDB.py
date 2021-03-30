import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3-v1')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from social_app_userprofile"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print "Total users: ", len(records)
        for row in records:
            print row[4]
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
readSqliteTable()