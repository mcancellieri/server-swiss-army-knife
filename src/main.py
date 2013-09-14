#!/usr/bin/python

import sys
from PyQt4 import *
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from AbstractConverter import AbstractConverter
import os
import plugin_loader as plugin_loader

class Gui(QWidget):
	
    def eventFilter(self,sender,event):
        if (event.type() == QtCore.QEvent.KeyPress):
            print(event.type())
            if (event.matches(QtGui.QKeySequence.Paste)):
                    buttonText = self.choosedType
                    converter = self.searchConverter(buttonText)                       
                    text = self.clipboard.text().toAscii()
                    self.textArea.clear()
                    output = converter.convert(self,text)
                    self.cursor.insertText(output)
                    return True
        return False

    def searchConverter(self, buttonText):
        print (self.plugins)
        for p in plugin_loader.getPlugins():
            plugin = plugin_loader.loadPlugin(p)
            print (plugin.getName(self))
            if plugin.getName(self) == buttonText:
                return plugin
                
            

    def toggle_function(self, pressed):
        source = self.sender()
        print source.text()
        if pressed:
            val = 255
        else: val = 0

        for button in self.button:
            if button.text()!=source.text():
                button.setChecked(False)

        self.choosedType=str(source.text())


    def setup_button(self, button, index):
         button.setCheckable(True)
         button.clicked[bool].connect(self.toggle_function)
         print 100 * (index+1)+5
         button.move(100 * (index)+5,0)

    def highLightText(self, text):
        cursor = self.cursor
        if text=='':
            return
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        cursor.setPosition(0)
        cursor.mergeCharFormat(format)
        # Setup the regex engine
        pattern = self.searchBox.text()
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.textArea.toPlainText(), pos)
        while (index != -1):
           # Select the matched text and apply the desired format
           cursor.setPosition(index)
           cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
           cursor.mergeCharFormat(format)
           # Move to the next match
           pos = index + regex.matchedLength()
           index = regex.indexIn(self.textArea.toPlainText(), pos)



    def __init__(self):
        print(self)
        QWidget.__init__(self, parent=None)
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(), screen.height()/2)
        self.move((screen.width() - self.geometry().width()) / 2, 0)
        self.textArea = QTextEdit(self)
        self.textArea.move(5,40)
        self.clipboard = QtGui.QApplication.clipboard()
        self.textArea.resize(screen.width(), screen.height()/2)
        self.cursor = QTextCursor(self.textArea.document())
        self.textArea.installEventFilter(self)
        self.button = []
        i = 0
        self.plugins = []
        for p in plugin_loader.getPlugins():
            plugin = plugin_loader.loadPlugin(p)
            self.button.append(QtGui.QPushButton(plugin.getName(self), self))
            self.setup_button(self.button[i], i)
            i+=1
        if len(self.button) > 0:
            self.choosedType = self.button[0].text()
            self.button[0].setChecked(True)
        self.searchBox = QLineEdit(self)
        self.searchBox.textChanged.connect(self.highLightText)
        self.searchBox.move(self.width()-150, 0)
        self.show()
        self.cursor.insertHtml("<a href='http://www.w3schools.com/'>Link!</a>")
        self.cursor.insertText("something")

class Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self, parent=None)
		self.gui = Gui()
        



app = QtGui.QApplication(sys.argv)
window = Main()
sys.exit(app.exec_())
