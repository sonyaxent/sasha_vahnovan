# coding=utf-8

import datetime
import pprint
import random
import string
from http import HTTPStatus

import pandas as pd
import requests
from flask import Flask, jsonify, Response
from webargs import validate, fields
from webargs.flaskparser import use_kwargs
from faker import Faker
from datetime import datetime
from database_handler import execute_query
from utils import format_records


app = Flask(__name__)


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ['Invalid request.'])

    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    else:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
        )


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# ДЗ 5. Початок ООП

class Circle:
    def __init__(self, centr_x, centr_y, radius):
        self.centr_x = centr_x
        self.centr_y = centr_y
        self.radius = radius

    def contains(self, x, y):
        return (x - self.centr_x) ** 2 + (y - self.centr_y) ** 2 < self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


krug = Circle(centr_x=1, centr_y=2, radius=50)

tochka = Point(x=2, y=3)

print(f'Вот результат: {krug.contains(tochka.x, tochka.y)}')


@app.route('/stats_by_city')
@use_kwargs(
    {
        'genre': fields.String(load_default="Rock",
                               validate=[validate.Regexp("[a-zA-Z]")]
                               )
    },
    location='query'
)
def stats_by_city(genre="Rock"):
    genres_list = ["Rock", "Jazz", "Metal", "Alternative & Punk", "Rock And Roll", "Blues", "Latin", "Reggae", "Pop", "Soundtrack", "Bossa Nova", "Easy Listening", "Heavy Metal", "R&B/Soul", "Electronica/Dance", "World", "Hip Hop/Rap", "Science Fiction", "TV Shows", "Sci Fi & Fantasy", "Drama", "Comedy", "Alternative", "Classical"]
    query = f"SELECT * FROM (SELECT genres.Name, invoices.BillingCity, sum(invoices.Total) as sum_total FROM genres INNER JOIN tracks ON genres.GenreId=tracks.GenreId INNER JOIN invoice_items ON tracks.TrackId=invoice_items.TrackId INNER JOIN invoices ON invoice_items.InvoiceId=invoices.InvoiceId group by genres.Name, invoices.BillingCity having genres.Name='{genre}') order by sum_total desc limit 1--"
    records = execute_query(query)
    if genre not in genres_list:
        return "Error: No Such Genre"
    else:
        return format_records(records)


if __name__ == "__main__":
    app.run(port=5001, debug=True)

