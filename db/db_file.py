#-*- coding:utf-8 -*-
#Author: Guangjie Guo

import sqlite3,os


def ins_sql(username,password):
    conn = sqlite3.connect('openfile.db')

    cursor = conn.cursor()

    # cursor.execute('create table user (id INTEGER PRIMARY KEY autoincrement ,name varchar(20), passwd varchar(20))')

    cursor.execute('insert into user (name,passwd) values ("%s","%s")'%(username,password))

    cursor.close()

    conn.commit()

    conn.close()


def del_sql(username):
    conn = sqlite3.connect('openfile.db')

    cursor = conn.cursor()

    # cursor.execute('create table user (id INTEGER PRIMARY KEY autoincrement ,name varchar(20), passwd varchar(20))')

    cursor.execute('delete from user where name = "%s"'% username)

    cursor.close()

    conn.commit()

    conn.close()

def cre_sql():
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conn = sqlite3.connect('openfile.db')

    cursor = conn.cursor()

    cursor.execute('create table user (id INTEGER PRIMARY KEY autoincrement ,name varchar(20) , passwd varchar(20))')

    cursor.close()

    conn.commit()

    conn.close()

def sel_sql():

    conn = sqlite3.connect('openfile.db')

    cursor = conn.cursor()

    cursor.execute('select * from user')

    values = cursor.fetchall()

    cursor.close()

    conn.close()

    return values

# import sqlite3
#
#
# def con_sql():
#     conn = sqlite3.connect('openfile.db')
#
#     return conn
#
#
# def clo_sql():
#     sql().close()
#
#     con_sql().close()
#
#
# def sql():
#     cursor = con_sql().cursor()
#
#     return cursor
#
#
# def ins_sql(username, password):
#     sql().execute('insert into user (name,passwd) values ("%s","%s")' % (username, password))
#
#     clo_sql()
#
#
# def del_sql(username):
#     sql().execute('delete from user where name = "%s"' % username)
#
#     clo_sql()
#
#
# def cre_sql():
#     sql().execute(
#         'create table user (id INTEGER PRIMARY KEY autoincrement ,name varchar(20) UNIQUE , passwd varchar(20))')
#
#     clo_sql()
#
#
# def sel_sql():
#     sql().execute('select * from user')
#
#     values = sql().fetchall()
#
#     clo_sql()
#
#     return values
