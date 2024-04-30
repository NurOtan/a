import psycopg2
import csv
from phone_book.config import host, user, password, db_name

# SQL queries
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phonenumber VARCHAR(20)
);
"""
delrow1 = "DELETE FROM users WHERE name = %s;"
delrow2 = "DELETE FROM users WHERE phonenumber = %s;"
delrow3 = "DELETE FROM users WHERE id = %s;"
addrow = "INSERT INTO users (name, phonenumber) VALUES (%s, %s)"


def create_table():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
        connection.commit()
    except Exception as ex:
        print("[INFO] Error while creating 'users' table:", ex)
    finally:
        if connection:
            connection.close()


def choose_action():
    while True:
        print('выберите что хотите сделать с телефонным справочником')
        print('1-добавить в справочник номер')
        print('2-убрать номер из справочника')
        print('3-просмотреть весь справочник номеров')
        print('4-изменить значение имени или номера')
        print('5-выйти из справочника')
        a = int(input())

        if a == 1:
            print('добавить через csv или вручную?')
            print('1-вручную')
            print('2-через csv')
            t = int(input())
            if t == 1:
                print('Введите имя и номер:')
                name = input()
                phonenumber = input()  # Assuming the phone number can contain non-numeric characters
                values = (name, phonenumber)
                try:
                    connection = psycopg2.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=db_name
                    )
                    connection.autocommit = True
                    with connection.cursor() as cursor:
                        cursor.execute(addrow, values)
                except Exception as ex:
                    print("[INFO] Error while adding entry to 'users' table:", ex)
                finally:
                    if connection:
                        connection.close()
                        print("[INFO] PostgreSQL connection closed")

            elif t == 2:
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    try:
                        connection = psycopg2.connect(
                            host=host,
                            user=user,
                            password=password,
                            database=db_name
                        )
                        connection.autocommit = True
                        with connection.cursor() as cursor:
                            for row in reader:
                                name, phonenumber = row
                                values = (name, phonenumber)
                                cursor.execute(addrow, values)
                    except Exception as ex:
                        print("[INFO] Error while adding entries from CSV to 'users' table:", ex)
                    finally:
                        if connection:
                            connection.close()
                            print("[INFO] PostgreSQL connection closed")

        elif a == 2:
            print('1-удаление по имени')
            print('2-удаление по номеру')
            print('3-удаление по id')
            b = int(input())
            if b == 1:
                d = input()
            else:
                d = input()  # Assuming the user provides the phone number or id as input
            values = (d,)
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                connection.autocommit = True
                with connection.cursor() as cursor:
                    if b == 1:
                        cursor.execute(delrow1, values)
                    elif b == 2:
                        cursor.execute(delrow2, values)
                    elif b == 3:
                        cursor.execute(delrow3, values)
            except Exception as ex:
                print("[INFO] Error while deleting entry from 'users' table:", ex)
            finally:
                if connection:
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")

        elif a == 3:
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                connection.autocommit = True
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM users"""
                    )

                    for row in cursor.fetchall():
                        print(row)
            except Exception as ex:
                print("[INFO] Error while fetching entries from 'users' table:", ex)
            finally:
                if connection:
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")

        elif a == 4:
            print('найти нужную строку по:')
            print('1-имени')
            print('2-номеру')
            print('3-id')
            t = int(input())
            print('что нужно изменить?')
            print('1-имя')
            print('2-номер')
            m = int(input())
            print('введите обновленный текст')
            v = input()
            print('введите данную которую нужно поменять')
            tr = input()
            values = (v, tr)
            if t == 1:
                if m == 1:
                    query = "UPDATE users SET name = %s WHERE name = %s;"
                else:
                    query = "UPDATE users SET phonenumber = %s WHERE name = %s;"
            elif t == 2:
                if m == 1:
                    query = "UPDATE users SET name = %s WHERE phonenumber = %s;"
                else:
                    query = "UPDATE users SET phonenumber = %s WHERE phonenumber = %s;"
            elif t == 3:
                if m == 1:
                    query = "UPDATE users SET name = %s WHERE id = %s;"
                else:
                    query = "UPDATE users SET phonenumber = %s WHERE id = %s;"
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                connection.autocommit = True
                with connection.cursor() as cursor:
                    cursor.execute(query, values)
            except Exception as ex:
                print("[INFO] Error while updating entry in 'users' table:", ex)
            finally:
                if connection:
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")

        elif a == 5:
            print('программа завершена')
            break


if __name__ == "__main__":
    create_table()
    choose_action()