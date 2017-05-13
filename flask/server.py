# -*- coding: utf-8 -*-
import sys
import os
from flask import Flask, render_template, request

appweb = Flask(__name__)

print('Run Server')
appweb.run()


