# coding: utf-8
import sys
import os
import htmlPy


class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app
        self.prueba()

    @htmlPy.Slot()
    def say_hello_world(self):
        # self.app.html = u"Hello, world"
        # self.app.bind(BackEnd(self.app))
        self.css = os.path.abspath(os.path.dirname(__file__)) + u"\css\\style.css"
        self.app.template = ("index1.html", { 'css' : self.css })

    @htmlPy.Slot()
    def prueba(self):
        # self.app.html = u"<b>hola<b> que tal"
        self.app.template_path = "."
        self.css = os.path.abspath(os.path.dirname(__file__)) + u"\css\\style.css"
        self.app.template = ("index.html", { 'css' : self.css })

    @htmlPy.Slot()
    def home(self):
        # self.app.html = u"<b>hola<b> que tal"
        self.app.template_path = "."
        self.css = os.path.abspath(os.path.dirname(__file__)) + u"\css\\style.css"
        self.app.template = ("test.html", { 'css' : self.css })

    @htmlPy.Slot()
    def test(self):
        self.app.template_path = "."
        self.prueba = u"Andrés"
        self.app.template = ("index1.html", { 'prueba' : self.prueba }) 