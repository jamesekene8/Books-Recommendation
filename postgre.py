import eda
import psycopg2
import pandas as pd
import psycopg2.extras as extras
from dotenv import dotenv_values

config = dotenv_values(".env")


def insertingIntoPostgre():
    # establishing the connection
    conn = psycopg2.connect(
        database=config["DATABASE"], user=config["USER"], password=config["PASSWORD"], host='127.0.0.1', port=config["PORT"]
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = '''CREATE database amazon'''

    # Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    conn = psycopg2.connect(database="amazon",
                            user=config["DATABASE"], password=config["PASSWORD"],
                            host='127.0.0.1', port=config["PORT"]
                            )

    conn.autocommit = True
    cursor = conn.cursor()

    sql = '''CREATE TABLE books(title char(250),\
    url varchar(500), author varchar(150), year varchar(30), price float);'''

    cursor.execute(sql)

    print("Table created successfully........")

    def execute_values(conn, df, table):

        tuples = [tuple(x) for x in df.to_numpy()]

        cols = ','.join(list(df.columns))
        # SQL query to execute
        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = conn.cursor()
        try:
            extras.execute_values(cursor, query, tuples)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cursor.close()
            return 1
        print("the dataframe is inserted")
        cursor.close()

    execute_values(conn, eda.df, 'books')
