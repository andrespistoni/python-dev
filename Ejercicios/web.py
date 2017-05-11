import sys
sys.path.append("..")
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl
# import urllib.request
 
# sContenidoPagina = urllib.request.urlopen('/theme/index.html')

# print sContenidoPagina.read()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 320)
        self.setWindowTitle('PyQt-5 WebEngine')

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.web_view = QWebEngineView()
        self.web_view.load(QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'\test.html'))
        self.web_view.loadProgress.connect(self.webLoading)

        root = QVBoxLayout()
        root.addWidget(self.web_view)
        root.addWidget(self.progress)

        self.setLayout(root)

    def btnIrClicked(self, event):
        url = QUrl(self.url.text())
        self.web_view.page().load(url)

    def webLoading(self, event):
        self.progress.setValue(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())












# import sys
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtWidgets import QApplication

# class Browser(QWebEngineView):

#     def __init__(self):
#         QWebEngineView.__init__(self)
#         self.loadFinished.connect(self._result_available)

#     def _result_available(self, ok):
#         frame = self.page().mainFrame()
#         print(unicode(frame.toHtml()).encode('utf-8'))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     view = Browser()
#     view.load(QUrl('http://www.google.com'))
#     app.exec_()