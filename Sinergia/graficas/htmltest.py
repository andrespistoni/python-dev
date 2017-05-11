import sys
import os

class html_Web(object):
    def __init__(self, parent=None):
        # super(html_Web, self).__init__(parent=parent)
        self.html_top = """
                <!DOCTYPE html>
                <html lang="en">

                <head>

                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
                    """

        self.html_mid = '''
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
        self.cssopen = '<link rel="stylesheet" type="text/css" href="'
        self.cssclose = '">'
        self.cssfile = os.path.abspath(os.path.dirname(__file__)) + "\css\\style.css"
        self.cssline = self.cssopen + self.cssfile + self.cssclose

        self.htmltext = self.html_top + self.cssline + self.html_mid

    def armar_Html(self):
        self.html_file = open("test2.html", "w")
        self.html_file.write(self.htmltext)
        self.html_file.close()