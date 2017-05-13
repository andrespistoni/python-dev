# -*- coding: utf-8 -*-
import sys
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from json import dumps

appweb = Flask(__name__)

def servRun():
    print('Run Server')
    appweb.run()

def salir():
    func = request.environ.get('werkzeug.server.shutdown')
    func()    

@appweb.route('/login', methods=['GET'])
def login():

    return render_template('login.html')

@appweb.route(r'/usuario/add', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST': 

        var0 = request.form['user']
        var1 = request.form['name']
        var2 = request.form['email']
        var3 = request.form['password']
        return jsonify(user=var0, name=var1, email=var2, password=var3)

    if request.method == 'GET':
        return render_template('registro.html')

    return "No soy ninguno"

@appweb.route(r'/', methods=['GET'])
def index():
    return render_template('index.html')
