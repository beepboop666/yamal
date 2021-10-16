# -*- coding: utf-8 -*-
# Created by Danil Sviridov

from dbWorker import *
from relgive import *


def tape(hash):
    user_liked_genres = get_user_genres(hash)
    user_liked_authors = get_user_authors(hash)
    user_readed_t = get_user_readed(hash)
    user_readed = []
    for i in user_readed_t:
        t = [i['genre'], i['author']]
        user_readed.append(t)

    books_t = get_book_list('D', 'name', 'asc', get_user_age(hash), 'all', 'all')
    books = []
    for i in books_t:
        t = [i['genre'], i['author'], i['rate'], i['hash']]
        books.append(t)
    genres
    authors
