import psycopg2, os
from dotenv import load_dotenv
load_dotenv()

pgUser = os.environ.get("PGUSER")
pgHost = os.environ.get("PGHOST")
pgDatabase = os.environ.get("PGDATABASE")
pgPassword = os.environ.get("PGPASSWORD")
pgPort = os.environ.get("PGPORT")

def db_connect():
    try:
        conn = psycopg2.connect(database=pgDatabase,
                                user=pgUser,
                                password=pgPassword,
                                host=pgHost,
                                port=pgPort)
        return conn
    except Exception as e:
        print(str(e))
        raise


def create_table():
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS values (number INT)""")
        conn.commit()
        conn.close()
    except Exception as e:
        print(str(e))
        raise


def get_all_values():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM values""")
    data = cursor.fetchall()
    conn.close()
    return data


def insert_new_index(index):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO values(number) VALUES({})""".format(index))
    conn.commit()
    conn.close()
