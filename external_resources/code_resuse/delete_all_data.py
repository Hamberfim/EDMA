# -*- coding: utf-8 -*-
"""
Created on 7/14/2020	
@author: Anthony Hamlin
Program: delete_all_data.py

This program deletes ALL data from the person table in the pythonsqlite.db
database file (unless WHERE is used to limit the criteria)
!!!! SEE delete_all_person below before running !!!!
"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows # return the rows


def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows # return the rows


def delete_person(conn, id):
    """Delete a person by person id
    :param conn: database connection
    :param id: id of the person
    :return:
    """
    sql = 'DELETE FROM person WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_all_person(conn):
    """Delete all rows in the person table
    :param conn: database connection
    :return:
    """
    sql = 'DELETE FROM person # WHERE #'
    cur = conn.cursor()
    cur.execute(sql)


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:

        delete_person(conn, 1)
        rows = select_all_persons(conn)
        for row in rows:
            print(row)
