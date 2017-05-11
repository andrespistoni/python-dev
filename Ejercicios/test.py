import sys
import os
from PyQt5.QtCore import QUrl



cssopen = '<link rel="stylesheet" type="text/css" href="'
cssclose = '">'
cssfile = os.path.abspath(os.path.dirname(__file__)) + "\css\\style.css"
cssline = cssopen + cssfile + cssclose
print(os.path.abspath(os.path.dirname(__file__)) + "\css\\style.css")