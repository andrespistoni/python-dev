# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl, Qt
from flask import redirect, url_for
import multiprocessing
import imp

class MyProcess(multiprocessing.Process):
    def __init__(self,thing):
        multiprocessing.Process.__init__(self)
        self.thing=thing

    def run(self):
        print('running...', self.thing())

class Begin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('PyQt-5 WebEngine')

        self.progress = QProgressBar()
        self.progress.setValue(0)
        
        self.module=imp.load_source('rout', './rout.py')
        self.thing=self.module.servRun
        self.p=MyProcess(self.thing)
        self.p.start()

        self.web_view = QWebEngineView()
        self.web_view.load(QUrl('http://127.0.0.1:5000'))
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

    def closeEvent(self, event):
        self.p.terminate()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Begin()
    win.show()
    sys.exit(app.exec_())
