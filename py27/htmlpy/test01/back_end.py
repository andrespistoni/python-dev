import htmlPy
# from flask import *

class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
        self.app.html = u'''
                        <b>hola<b> que tal
                        <br>
                        <a
                            href="BackEnd.page1"
                            data-bind="true">
                            Click to show page1
                        </a>
                        <a
                            href="BackEnd.page1"
                            data-bind="true">
                            Click to show page1
                        </a>
                        '''

    @htmlPy.Slot()
    def prueba(self):
        self.app.html = u'''
                        <b>hola<b> que tal
                        <br>
                        <a
                            href="BackEnd.say_hello_world"
                            data-bind="true">
                            Click to say "Hello, world"
                        </a>
                        <br/>
                        <a
                            href="BackEnd.page1"
                            data-bind="true">
                            Click to show page1
                        </a>

                        '''
    @htmlPy.Slot()
    def page1(self):
        self.app.html = u'''
                            <h1>page1</h1>
                            <a
                                href="BackEnd.say_hello_world"
                                data-bind="true">
                                Click to say "Hello, world"
                            </a>
                            <br/>
                            <a
                                href="BackEnd.prueba"
                                data-bind="true">
                                Click otra cosa
                            </a>
                        '''

# import htmlPy
# # from flask import *


# class BackEnd(htmlPy.Object):
#     @htmlPy.Slot()
#     def say_hello_world(self):
#         self.app.html = u"Hello, world"
#     @htmlPy.Slot()
#     #@app.route('/page1')
#     def page1(self):
#         return '''<h1>page1</h1>'''
