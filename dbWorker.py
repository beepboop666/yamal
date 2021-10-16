# -*- coding: utf-8 -*-
# Created by Danil Sviridov
import datetime
import json
import pymysql
from hashlib import md5
from dateutil import parser


# __________________________________
# service block


def connect(user='D'):
    if user == 'D':
        return pymysql.connect(user='root', password='password', db='yamal', host='localhost')
    elif user == 'S':
        return pymysql.connect(user='root', password='0211AlGr', db='yamal', host='localhost')
    return 'Invalid user, try S (Sasha) or D (Danil)'


# __________________________________
# books block


def get_book_list(dbOwner, sortBy='name', order='asc', age=0, genre='all', author='all'):
    genres = ['Зарубежная литература', 'Фантастика', 'Современная проза', 'Детективы', 'Фэнтези', 'История',
              'Психология и мотивация', 'Любовные романы', 'Публицистика', 'Русская классика', 'Спорт и здоровье',
              'Биография']
    dictionary = ['name', 'author', 'genre', 'rate']
    connection = connect(dbOwner)
    if sortBy not in dictionary:
        sortBy = 'name'
    if order not in ['asc', 'desc']:
        order = 'asc'
    dop = ''
    if genre == 'all':
        dop = '(1 == 1)'
    elif genre in genres:
        dop = f"(genre == '{genre}')"
    aut = ''
    if author == 'all':
        aut = '(1 == 1)'
    else:
        aut = f"(author == '{author}'"
    sql = f'SELECT * FROM books WHERE ages <= {age} and {dop} and {aut} ORDER BY {sortBy} {order}'
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    ret = []
    for i in data:
        if i[7] == 1:
            tmp = {'name': i[0], 'author': i[1], 'genre': i[2], 'rate': i[8], 'hash': i[5]}
            ret.append(tmp)
    return ret


def get_book_info(hash):
    connection = connect()
    sql = f"SELECT * FROM books WHERE hash == '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    t = data[0]
    ret = {'name': t[0], 'author': t[1], 'genre': t[2], 'ages': t[5], 'rate': t[8], 'about': t[9]}
    return ret


def get_reviews(hash):
    connection = connect()
    sql = f"SELECT reviews FROM books WHERE hash == '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    rev = data[0][0]
    ret = json.loads(rev)
    return ret


# __________________________________
# auth block


def check_mail(email):
    connection = connect()
    sql = f"SELECT COUNT(*) FROM user WHERE email = '{email}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return data[0][0] == '1'


def add_tmp_pass(email, code):
    connection = connect()
    if check_mail(email):
        sql = f"UPDATE user SET lastpass = '{code}' WHERE email = '{email}'"
        with connection.cursor() as cur:
            cur.execute(sql)
        connection.close()
        return 'Success'
    else:
        sql = f"INSERT INTO user (email, code) VALUES('{email}', '{code}')"
        with connection.cursor() as cur:
            cur.execute(sql)
        connection.close()
        return 'New user'


def check_tmp_pass(email, code):
    connection = connect()
    sql = f"SELECT lastpass FROM user WHERE email = '{email}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    if str(code) != data[0][0]:
        return False
    return True


# __________________________________
# user block


def get_user_hash(email):
    connection = connect()
    sql = f"SELECT hash FROM user WHERE email = '{email}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return data[0][0]


def user_fill_fields(email, name, surname, birth, genres, authors):
    u = email + name + surname + birth
    h = md5(u).hexdigest()
    g = str(genres)
    a = str(authors)
    connection = connect()
    sql = f"UPDATE user SET name='{name}', surname='{surname}', birth='{birth}', hash='{h}', genres='{g}', " \
          f"authors='{a}' WHERE email='{email}'"
    with connection.cursor() as cur:
        cur.execute(sql)
    connection.close()
    return h


def get_user_age(hash):
    connection = connect()
    sql = f"SELECT birth FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    t = parser.parse(data[0][0])
    a = datetime.datetime.now() - t
    age = a.days / 365
    return age


def get_user_genres(hash):
    connection = connect()
    sql = f"SELECT genres FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return json.loads(data[0][0])


def get_user_authors(hash):
    connection = connect()
    sql = f"SELECT authors FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return json.loads(data[0][0])


def get_user_liked(hash):
    connection = connect()
    sql = f"SELECT liked FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return json.loads(data[0][0])


def get_user_goals(hash):
    connection = connect()
    sql = f"SELECT goals FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return json.loads(data[0][0])


def get_user_readed(hash):
    connection = connect()
    sql = f"SELECT readed FROM user WHERE hash = '{hash}'"
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    return json.loads(data[0][0])


# __________________________________
# dop block


def get_genres_list():
    connection = connect()
    sql = 'SELECT name FROM genres'
    with connection.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    connection.close()
    ret = []
    for i in data:
        ret += i[0]
    return ret


# __________________________________
# order block
