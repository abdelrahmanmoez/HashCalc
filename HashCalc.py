'''
@author: Abdelrahman Moez - aka Hydra
@script: HashCalc.py
@description: This script gives you the MD5, SHA1 and SHA256 hashes of a given file
@python version: 2.7
'''
import sys
from PyQt4 import QtGui, QtCore
import hashlib

class HashCalc(QtGui.QWidget):
    
    def __init__(self):
        super(HashCalc, self).__init__()
        self.UI()
        self.file_path = ""        
        
    def UI(self):  
        # Browser file
        browse_label = QtGui.QLabel('File Path', self)
        browse_label.move(20,30)
        
        browse_btn = QtGui.QPushButton("Browse", self)
        browse_btn.move(380, 30)
        browse_btn.clicked.connect(self.browseFile)

        self.browse_line = QtGui.QLineEdit(self)
        self.browse_line.move(100,30)
        self.browse_line.setReadOnly(True)
        self.browse_line.resize(250,25)
        # MD5 Label
        md5_label = QtGui.QLabel('MD5', self)
        md5_label.move(20,75)

        self.md5_line = QtGui.QLineEdit(self)
        self.md5_line.move(100,70)
        self.md5_line.resize(250,20)
        self.md5_line.setReadOnly(True)
        # SHA1 Label
        sha1_label = QtGui.QLabel('SHA1', self)
        sha1_label.move(20,105)

        self.sha1_line = QtGui.QLineEdit(self)
        self.sha1_line.move(100,100)
        self.sha1_line.resize(250,20)
        self.sha1_line.setReadOnly(True)
        # SHA256 label
        sha256_label = QtGui.QLabel('SHA256', self)
        sha256_label.move(20,135)

        self.sha256_line = QtGui.QLineEdit(self)
        self.sha256_line.move(100,130)
        self.sha256_line.resize(250,20)
        self.sha256_line.setReadOnly(True)
        #'''
        calc = QtGui.QPushButton("Calculate", self)
        calc.move(380, 130)
        calc.clicked.connect(self.buttonClicked)
        #
        
        self.setGeometry(300, 300, 500, 180)
        self.setWindowTitle('Hash Calculater - version 1.0')
        self.show()
    def buttonClicked(self):
        f = open(self.file_path, 'rb')
        file_content = f.read()
        f.close()
        #print file_content
        md5_enc_data = hashlib.md5(file_content).hexdigest()
        sha1_enc_data = hashlib.sha1(file_content).hexdigest()
        sha256_enc_data = hashlib.sha256(file_content).hexdigest()
        
        self.md5_line.setText(md5_enc_data)
        self.sha1_line.setText(sha1_enc_data)
        self.sha256_line.setText(sha256_enc_data)

    def browseFile(self):
        file_path = QtGui.QFileDialog.getOpenFileName(self, "Open Data File", "", "(*.*)")
        self.file_path = file_path
        self.browse_line.setText(file_path)
        return file_path
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = HashCalc()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
