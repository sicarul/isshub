#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
isshub
Github issues client
Using python with qt4

author: Pablo Alejandro Seibelt
website: www.sicarul.com.ar
last edited: December 2013
"""

import sys
from PyQt4 import QtGui, QtCore


class NewIssue(QtGui.QMainWindow):
    
    def __init__(self):
        super(NewIssue, self).__init__()
        
        self.initUI()

    def createissue(self):
    	#curl -H "Authorization: token 3d846b63a81730fd5651b3f8184dd932664704fc" https://api.github.com
    	pass
        
    def initUI(self):               
        

        self.statusBar().showMessage('')

        cw = QtGui.QWidget()
        self.setCentralWidget(cw)

        txt_reponame = QtGui.QLineEdit (self)
        txt_reponame.setToolTip('The <b>new issue\'s</b> complete repository name (user/repository)')
        txt_reponame.setText('sicarul/isshub')

        txt_issname = QtGui.QLineEdit (self)
        txt_issname.setToolTip('The <b>new issue\'s</b> title')
        txt_issname.setText('Test issue')

        txt_issdesc = QtGui.QTextEdit (self)
        txt_issdesc.setToolTip('A description of the issue')
        txt_issdesc.setText('This is just a test issue')

        btn_create = QtGui.QPushButton ('Create issue',self)
        btn_create.setToolTip('Create the issue')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_create)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(txt_reponame)
        vbox.addWidget(txt_issname)
        vbox.addWidget(txt_issdesc)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        cw.setLayout(vbox) 
        self.setGeometry(200, 200, 800, 300)
        self.center()
        self.setWindowTitle('isshub - New issue')    
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = NewIssue()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()   
