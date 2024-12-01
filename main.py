from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import sys 

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)

        self.current_path = None
        self.current_fonsize = 8
        self.setWindowTitle("Untitled")

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.save_asFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionIncrease_Font_Size.triggered.connect(self.incFontSize)
        self.actionDecrease_Font_Size.triggered.connect(self.decFontSize)
        self.actionSet_To_Bold.triggered.connect(self.setToBold)
        self.actionAbout_Text_Editor.triggered.connect(self.aboutTextEditor)
        self.actionContact_Us.triggered.connect(self.contactUs)
    
    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None


    def saveFile(self):
        if self.current_path is not None:
            #save the changes of file without opening dialog
            file_text = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(file_text)
        else:
            self.save_asFile()
        
        
        
    def save_asFile(self):
        path_name = QFileDialog.getSaveFileName(self, 'Save file', 
                                                r"C:\Users\cabdo\Desktop\Python-GUI-Projects\PyQt5 Text Editor", 
                                                'Text files(*.txt)')
        file_text = self.textEdit.toPlainText()
        with open(path_name[0], 'w') as f:
            f.write(file_text)
        self.current_path = path_name[0]
        self.setWindowTitle(path_name[0])

        



    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
                                            r"C:\Users\cabdo\Desktop\Python-GUI-Projects\PyQt5 Text Editor",
                                            'Text file (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0], 'r') as f:
            file_text = f.read()
            self.textEdit.setText(file_text)
        self.current_path = fname[0]


    def undo(self):
        self.textEdit.undo()


    def redo(self):
        self.textEdit.redo()


    def cut(self):
        self.textEdit.cut()


    def copy(self):
        self.textEdit.copy()


    def paste(self):
        self.textEdit.paste()


    def setDarkMode(self):
        self.setStyleSheet('''QWidget{
        background-color: rgb(33, 33, 33); /* black color*/
        color: #FFFFFF; /* I think white color*/
        }
        QTextEdit{
        background-color: rgb(46, 46, 46);/* grey color*/
        }
        QMenuBar::item:selected{
        color: #000000 ; /*black color*/
        }

        ''')


    def setLightMode(self):
        self.setStyleSheet("")


    def incFontSize(self):
        self.current_fonsize += 1
        self.textEdit.setFontPointSize(self.current_fonsize)


    def decFontSize(self):
        self.current_fonsize -= 1
        self.textEdit.setFontPointSize(self.current_fonsize)

    def setToBold(self):
        self.textEdit.setStyleSheet("font-weight: bold")


    def aboutTextEditor(self):
        message = QMessageBox()
        message.setWindowIcon(QIcon('logo.png'))
        message.setWindowTitle("About This Text Editor")
        #message.setGeometry(60, 60, 600, 400)
        message.setFixedSize(600, 300)
        message.setStandardButtons(QMessageBox.Ok)
        message.setText("This Text Editor is made by me through practice\n I'm Abdihalim \n You can reach me \n in GitHub Abdihalim-codes")
        message.exec_()

    def contactUs(self):
        message = QMessageBox()
        message.setWindowTitle("Contact Us")
        message.setText("For inquiries, please contact us:\nEmail: cabdooo19@.com\nPhone: (251) 943-921-921")
        message.setIcon(QMessageBox.Information)
        message.setWindowIcon(QIcon('logo.png'))
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()