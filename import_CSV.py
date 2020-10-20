import sqlite3
import sys
import csv

def import_csv(filename_path):
    file = open(filename_path)
    fileRead = csv.reader(file)
    fileData = list(fileRead)

    return fileData


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


    preces = import_csv('preces.csv')

    #for x, y in preces:
        #print(x.strip(), y)
        #q2 = 'INSERT INTO preces (nosaukums, kateg_id) VALUES (?, ?)'
        #cursor.execute(q2, (x.strip(), y,))
        #connection.commit()


    kategorijas = import_csv('kategorijas.csv')
    listToStr = ' '.join(map(str, kategorijas))
    #print(listToStr)

    # for x in kategorijas:
    #     kat = ' '.join(map(str, x))
    #     print(kat)
    #     q3 = 'INSERT INTO kategorijas (kategorija) VALUES (?)'
    #     cursor.execute(q3, (kat,))
    #     connection.commit()


    cursor.execute(
    "SELECT p.prece_id, p.nosaukums, kategorija FROM preces p JOIN kategorijas k"
    " ON p.kat_id = k.kat_id"
    )


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
