import sqlite3
import sys


#def import_csv():


def sql_ide(connection, cursor, opt):
    if (opt != 'q'): print("Starting SQLite ID")
    while opt != 'q':
        try:
            opt = input()
            cursor.execute(opt).fetchall()
            for x in cursor:
                print(x)

            connection.commit()
            opt = input()

        except sqlite3.Error as error:
            print("Error executing orders.", error)


try:
    connection = sqlite3.connect('SQLite_Python.db')
    cursor = connection.cursor()

    opt = str(sys.argv[1]) if len(sys.argv) > 1 else ""
    sql_ide(connection, cursor, opt)


    for prece, id in preces:
        q2 = 'INSERT INTO preces (nosaukums, kateg_id) VALUES (?, ?)'
        cursor.execute(q2, (prece, id,))
        connection.commit()





    cursor.execute("SELECT * FROM preces")
    for x in cursor:
        print(x)

    cursor.close()
    print("Operation successful")

except sqlite3.Error as error:
    print("Error:", error)
finally:
    if (connection):
        connection.close()
        print("sqlite connection is closed")
