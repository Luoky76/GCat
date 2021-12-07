import json
import requests
import psycopg2
from github import Github

# curs = conn.cursor()
conn = psycopg2.connect(database='mydb', user='gx',
                        password='GaussDB@123', host='120.46.159.207', port=26000)

def inserthistory(token, full_name):
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    result = "failed"
    user_id = Github(token).get_user().id
    try:
        search_sql = "INSERT INTO history (userid, repo) VALUES ('{}','{}')".format(user_id, full_name)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        # print(type(result))
        # print(type(result[0]))
        # print(type(str(result[0])))
        # print(str(result[0])[2:])
        # result = str(result[0])[2:]
        conn.commit()
    except:
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return result

def searchhistory(token):
    global conn
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1')
    except psycopg2.OperationalError:
        conn = psycopg2.connect(database='mydb', user='gx',
                                password='GaussDB@123', host='120.46.159.207', port=26000)
    curs = conn.cursor()
    result = "failed"
    user_id = Github(token).get_user().id
    try:
        search_sql = "select repo from history where userid = '{}'".format(user_id)
        print(search_sql)
        curs.execute(search_sql)
        print(curs.rowcount)
        result = curs.fetchall()
        # print(type(result))
        # print(type(result[0]))
        # print(type(str(result[0])))
        # print(str(result[0])[2:])
        # result = str(result[0])[2:]
        conn.commit()
    except:
        print('发生错误')
        conn.rollback()
    finally:
        curs.close()
        return result