import sqlite3
import pandas as pd
import pandas_profiling
import html


DATABASE_NAME = 'SQLite_Python.db'
FILENAME = 'atskaite1.html'

def pp(operation):
    print(">> {}.".format(operation))


def print_table(cursor):
    for x in cursor:
        print(x)


try:
    pp("Connecting to database " + DATABASE_NAME)
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    pp("Creating query")
    q = '''SELECT p.nosaukums, kategorija
           FROM preces p JOIN kategorijas k
           ON p.kat_id = k.kat_id'''

    query = cursor.execute(q)

    pp("Query created")
    print(q)

    pp('Preparing Data Frame')
    df = pd.read_sql_query(q, connection)
    print(df)

    html = df.to_html()
    pp('df.to_html()')
    print(html)

    pp('Writting HTML to file')
    text_file = open(FILENAME, "w")
    text_file.write(html)
    text_file.close()

    pp('Start profiling')
    pandas_profiling.ProfileReport(df)




    cursor.close()
    print("Operation successful")

except sqlite3.Error as error:
    print("Error:", error)

finally:
    if (connection):
        connection.close()
        print("sqlite connection is closed")
