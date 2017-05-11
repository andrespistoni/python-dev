# -*- coding: utf-8 -*-
import sys
from flask import Flask, render_template, request

appweb = Flask(__name__)

def servRun():
    print('Run Server')
    appweb.run()

def salir():
    func = request.environ.get('werkzeug.server.shutdown')
    func()    

@appweb.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')

