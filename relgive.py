# -*- coding: utf-8 -*-

def relatve(account_data_genres, account_data_authors, readed_books_data, books_data, genres, authors):
    size_account_genres = len(account_data_genres)
    size_account_authors = len(account_data_authors)
    size = 7
    need_size = 20
    proc_of_genres = []
    for i in genres:
        count = 0.0
        readed_books_data_size = 0.0
        for j in readed_books_data:
            if j[0] == i:
                readed_books_data_size += 1
        if i in account_data_genres:
            count += (2 + (size - len(readed_books_data))) / size_account_genres
        count += size / (len(readed_books_data)) * readed_books_data_size
        proc_of_genres.append([i, count])
    proc_of_authors = []
    for i in authors:
        count = 0
        readed_authors_data_size = 0.0
        for j in readed_books_data:
            if j[1] == i:
                readed_authors_data_size += 1
        if i in account_data_authors:
            count += (2 + (size - len(readed_books_data))) / size_account_authors
        count += size / (len(readed_books_data)) * readed_authors_data_size
        proc_of_authors.append([i, count])
    final_books_data = []
    for i in books_data:
        for h in proc_of_genres:
            if h[0] == i[0]:
                k: float = h[1]
                break
        for h in proc_of_authors:
            if h[0] == i[1]:
                final_books_data.append([i[0], i[1], i[2] + k + h[1], i[3]])
                break
    final_books_data.sort(key=lambda x: x[2], reverse=True)
    return final_books_data[:need_size]
