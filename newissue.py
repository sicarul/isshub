#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
isshub
Github issues client
Using python with qt4

author: Pablo Alejandro Seibelt
website: www.sicarul.com.ar
"""

#Username - case sensitive, a-z A-Z 0-9 - (dash), cannot begin with dash
#Reponame - case sensitive, a-z A-Z 0-9 - (dash)

import sys
from PySide import QtGui, QtCore
import github_api


class NewIssue(QtGui.QMainWindow):
    
    def __init__(self):
        super(NewIssue, self).__init__()
        
        self.initUI()


    def showError(self, msg):
      QtGui.QMessageBox.about(self, "ERROR", "%s" % msg )
      

    def create_issue(self):
      reponame = self.txt_reponame.text()
      issname =  self.txt_issname.text()
      issdesc = self.txt_issdesc.toPlainText()

      status = github_api.create_issue(reponame, issname, issdesc)

      if status == "Ok":
        self.close()
      else:
        self.showError("An error has ocurred trying to create the issue: " + status)
      
        
    def initUI(self):               
        

        self.statusBar().showMessage('')

        self.cw = QtGui.QWidget()
        self.setCentralWidget(self.cw)

        self.txt_reponame = QtGui.QLineEdit (self)
        self.txt_reponame.setToolTip('The <b>new issue\'s</b> complete repository name (user/repository)')
        self.txt_reponame.setText('sicarul/isshub')

        self.txt_issname = QtGui.QLineEdit (self)
        self.txt_issname.setToolTip('The <b>new issue\'s</b> title')
        self.txt_issname.setText('Test issue')

        self.txt_issdesc = QtGui.QTextEdit (self)
        self.txt_issdesc.setToolTip('A description of the issue')
        self.txt_issdesc.setText('This is just a test issue')

        self.btn_create = QtGui.QPushButton ('Create issue',self)
        self.btn_create.setToolTip('Create the issue')
        self.btn_create.clicked.connect(self.create_issue)

        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.btn_create)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.txt_reponame)
        self.vbox.addWidget(self.txt_issname)
        self.vbox.addWidget(self.txt_issdesc)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        
        self.cw.setLayout(self.vbox) 
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
