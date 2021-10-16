import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flasgger import swag_from, Swagger
from passTemplate import gen_mail
from dbWorker import *
from flask import Flask, request

app = Flask(__name__)
app.config.from_pyfile('config.py')
swagger = Swagger(app)


@app.route('/reg', methods=['POST'])
@swag_from('models/reg.yml')
def reg():
    data = request.json
    t = user_fill_fields(data['email'], data['name'], data['surname'], data['birth'], data['genres'], data['authors'])
    return t


@app.route('/login', methods=['POST'])
@swag_from('models/login.yml')
def login():
    data = request.json
    sender_email = 'payment@xn--d1aasecdjbcbfd5c.xn--p1ai'
    sender_password = '1rtYu77489'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Вход в NorthBook"
    message["From"] = sender_email
    message["To"] = data['email']
    code = random.randint(100000, 999999)
    a = add_tmp_pass(data['email'], code)
    message.attach(MIMEText(gen_mail(code), 'html'))
    with smtplib.SMTP('smtp.beget.com', 2525) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, data['email'], message.as_string())
    if a == 'Success':
        response = app.response_class(response='Success', status=200)
    elif a == 'New user':
        response = app.response_class(response='New user', status=200)
    else:
        response = app.response_class(response='I\'m a teapot, not a coffeemaker', status=418)
    return response


@app.route('/confirm', methods=['POST'])
@swag_from('models/confirm.yml')
def confirm():
    data = request.json
    if check_tmp_pass(data['email'], data['code']):
        response = app.response_class(response=get_user_hash(data['email']), status=200)
    else:
        response = app.response_class(response='Invalid code', status=400)
    return response


@app.route('/books', methods=['POST'])
@swag_from('models/books.yml')
def books():
    data = request.json
    a = get_user_age(data['user'])
    if data['genre'] is None:
        data['genre'] = 'all'
    t = get_book_list('D', 'name', 'asc', a, data['genre'])
    t = app.response_class(t, status=200, mimetype='application/json')
    return t


@app.route('/bookabout', methods=['POST'])
@swag_from('models/bookabout.yml')
def bookabout():
    data = request.json
    t = get_book_info(data['hash'])
    return app.response_class(t, status=200, mimetype='application/json')


@app.route('/bookgetreviews', methods=['POST'])
@swag_from('models/bookgetreviews.yml')
def bookgetreviews():
    data = request.json
    t = get_reviews(data['hash'])
    return app.response_class(t, status=200, mimetype='application/json')


@app.route('/trends', methods=['POST'])
@swag_from('models/trends.yml')
def trends():
    data = request.json
    a = get_user_age(data['user'])
    r = []
    t = get_book_list(dbOwner='D', sortBy='rate', order='desc', age=a)
    i = 0
    for j in t:
        i += 1
        r.append(j)
        if i == 100:
            break
    t = app.response_class(t, status=200, mimetype='application/json')
    return t


if __name__ == '__main__':
    app.run()
