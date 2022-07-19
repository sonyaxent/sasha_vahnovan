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



# ДЗ 4. Flask + SQL

@app.route('/order_price')
@use_kwargs(
    {
        'country': fields.String(load_default="BillingCountry"
                                 )
    },
    location='query'
)
def order_price(country="BillingCountry"):
    if country == "BillingCountry":
        query = f'SELECT invoices.BillingCountry, invoice_items.InvoiceId, count(invoice_items.Quantity) * invoice_items.UnitPrice AS Order_Price_Total FROM invoice_items JOIN invoices ON invoice_items.InvoiceId=invoices.InvoiceId GROUP BY BillingCountry, invoice_items.InvoiceId HAVING BillingCountry={country}--'
        records = execute_query(query)

        return format_records(records)
    else:
        query = f'SELECT invoices.BillingCountry, invoice_items.InvoiceId, count(invoice_items.Quantity) * invoice_items.UnitPrice AS Order_Price_Total FROM invoice_items JOIN invoices ON invoice_items.InvoiceId=invoices.InvoiceId GROUP BY BillingCountry, invoice_items.InvoiceId HAVING BillingCountry="{country}"--'
        records = execute_query(query)

        return format_records(records)



@app.route('/get_all_info_about_track')
@use_kwargs(
    {
        'track_id': fields.String(load_default="tracks.TrackId"
                                  )
    },
    location='query'
)
def get_all_info_about_track(track_id="tracks.TrackId"):
    query = f"SELECT * FROM tracks INNER JOIN playlist_track ON tracks.TrackId=playlist_track.TrackId INNER JOIN albums ON tracks.AlbumId=albums.AlbumId INNER JOIN artists ON albums.ArtistId=artists.ArtistId WHERE tracks.TrackId={track_id}--"
    records = execute_query(query)

    return format_records(records)




if __name__ == "__main__":
    app.run(port=5001, debug=True)

