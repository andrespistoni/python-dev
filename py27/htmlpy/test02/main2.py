# coding: utf-8
import sys
import os
import htmlPy
from back_end import BackEnd
# css = os.path.abspath(os.path.dirname(__file__)) + u"\css\\style.css"

app = htmlPy.AppGUI(
    title=u"Sample application")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))
# css = os.path.abspath(os.path.dirname(__file__)) + u"\css\\style.css"
css = u'Hola'
app.template = ("index1.html", { 'css' : css })
# app.template = ("test.html", {} )

if __name__ == "__main__":
    app.start()