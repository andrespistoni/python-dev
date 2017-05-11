# coding: utf-8
# QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'\theme\index.html')

import sys
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1024, 768)
        self.setWindowTitle('PyQt-5 WebEngine')

        self.progress = QProgressBar()
        self.progress.setValue(0)

        html_top = """
                <!DOCTYPE html>
                <html lang="en">

                <head>

                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
                    """

        html_mid = '''
                    <title>Andrés Pistoni</title>

                </head>

                <body>

                    <section class="flex-center">
                        <div class="flex-container text-center">
                            <div class="img ">
                                <img src="Andrespistoni.jpg" alt="Andrés" class="circular" />
                            </div>
                            <div class="sig ">
                                <h1>Andrés Pistoni</h1>
                                <div class="desc">
                                    <h3>Arquitecto de Software en SAP-ABAP. <br/> Aprendiz de tecnologías Web, como NodeJs, Api-Rest, Socket.IO, Python, PHP, React.js, y más...</h3>
                                </div>
                                <hr />
                                <div class="content-social">
                                    <div class="colum-item-social">
                                        <div class="item-social">
                                            <a href="https://twitter.com/andrespistoni">
                                                <h4><i class="fa fa-twitter color" aria-hidden="true"></i>&nbsp;Twitter&nbsp;</h4>
                                            </a>
                                        </div>
                                        <div class="item-social">
                                            <a href="https://github.com/andrespistoni"
                                                <h4><i class="fa fa-github color" aria-hidden="true"></i>&nbsp;GitHub</h4>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="colum-item-social">
                                        <div class="item-social">
                                            <a href="https://plus.google.com/+AndresPistoni">
                                                <h4><i class="fa fa-google-plus color" aria-hidden="true"></i>&nbsp;Google+</h4>
                                            </a>
                                        </div>
                                        <div class="item-social">
                                            <a href="https://codepen.io/andrespistoni">
                                                <h4><i class="fa fa-codepen color" aria-hidden="true"></i>&nbsp;CodePen</h4>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <hr class="hr2">
                        </div>
                    </section>


                </body>

                </html>
        '''
        cssopen = '<link rel="stylesheet" type="text/css" href="'
        cssclose = '">'
        cssfile = os.path.abspath(os.path.dirname(__file__)) + "\css\\style.css"
        cssline = cssopen + cssfile + cssclose

        htmltext = html_top + cssline + html_mid

        html_file = open("test.html", "w")
        html_file.write(htmltext)
        html_file.close()

        self.web_view = QWebEngineView()
        self.web_view.loadProgress.connect(self.webLoading)
        self.web_view.load(QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/test.html'))
        
        root = QVBoxLayout()
        root.addWidget(self.web_view)
        root.addWidget(self.progress)

        self.setLayout(root)

    def webLoading(self, event):
        self.progress.setValue(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())