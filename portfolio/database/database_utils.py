import psycopg2
import os
import sys
import time

def connect_to_db(db='mysite'):
    conn = None
    try:
        print('Connecting to the database...')
        conn = psycopg2.connect(
            host='localhost',#os.getenv("HOST"),
            database='mysite',#os.getenv("DATABASE"),
            user='admin',#os.getenv("USERNAME"),
            password='password',#os.getenv("PASSWORD"),
        )
        print("-------------------------------------------------")
        print(f"You are now connected to {db}")
        print("-------------------------------------------------")
        return conn
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def insert_data(
    table_name, column_name, data_to_insert,
):
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"""
    INSERT INTO {table_name}({column_name})
    VALUES({data_to_insert});
    """
    cur.execute(query)    
    conn.commit()
    conn.close()
    print("Data has been inserted.")


def query_column_data(
    table_name, column_name,
):
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"""
    SELECT {column_name} FROM {table_name};
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("Data has been queried.")
    cur.close()
    conn.close()
    print("Connection closed.")
    return rows


def create_table(
    table_name, column_name,
    column_data_type
):
    conn = connect_to_db()
    cur = conn.cursor()
    query = f"""
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} (
        {table_name}_id SERIAL PRIMARY KEY,
    """
    for i in range(len(column_name)):
        if i is len(column_name)-1:
            query = query+column_name[i]+' '+column_data_type[i]+' NOT NULL);'
        else:
            query = query+column_name[i]+' '+column_data_type[i]+' NOT NULL, '
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()
    print('--------------')
    print('Table Created!')
    print('--------------')
