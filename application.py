#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/catalog/')
def showCategories():
    return 'show categories'

@app.route('/catalog/<int:catalog_id>/items')
def showItems():
    return 'show items'

@app.route('/catalog/<int:catalog_id>/<int:item_id>')
def showDesc():
    return 'show description'

@app.route('/catalog/new')
def newItem():
    return 'add new item'

@app.route('/catalog/<int:catalog_id>/<int:item_id>/edit')
def editItem():
    return 'edit item'

@app.route('/catalog/<int:catalog_id>/<int:item_id>/delete')
def deleteItem():
    return 'delete item'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
