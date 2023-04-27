import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def create_insert(conn, insert):
    sql = ''' INSERT INTO czytelnicy(imie,nazwisko,zapisany,wypozyczenia)
            VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, insert)
    conn.commit()
    
def select_instruction(conn, insert):
    cur = conn.cursor()
    text = insert
    cur.execute(text)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    return rows

def main():
    database = "bazasqlite.db"
    
    sql_create_czytelnicy_table = """ CREATE TABLE IF NOT EXISTS czytelnicy (
                                        imie text NOT NULL,
                                        nazwisko text NOT NULL,
                                        zapisany date,
                                        wypozyczenia integer
                                    );"""
    data = ('Adam','Kowalski','2018-10-13',3);
    datas = [('Ewa','Grabska','2017-09-14',5),
             ('Edward','Nowak','2019-03-11',7),
             ('Iwona','Krakowska','2016-12-17',2),
             ('Roman','Zdalny','2018-04-24',5),]
    
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn, sql_create_czytelnicy_table)
        for x in datas:
            create_insert(conn, x)
    else:
        print("Error! Cannot connect to database")
    select_instruction(conn,' SELECT imie,nazwisko,wypozyczenia FROM czytelnicy WHERE wypozyczenia > 3 ORDER BY wypozyczenia ASC ')
    print("\n")
    select_instruction(conn,' SELECT imie,nazwisko,wypozyczenia FROM czytelnicy WHERE wypozyczenia > 3 ORDER BY wypozyczenia DESC ')
    print("\n")
    result = select_instruction(conn,' SELECT * FROM czytelnicy ' )
    print("\n")
    print(result)
    conn.close()
    
if __name__ == '__main__':
    main()