from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp,self).__init__()
        self.setFixedSize(1000,500)
        self.setWindowTitle('N_gen')
        loadUi('gui/main.ui',self)
        
        # Buttons signals
        self.bt_search_notes.clicked.connect(lambda : self.search_dir(self.line_path_notes)) # Buscar la carpeta del cuaderno
        self.bt_search_templates.clicked.connect(lambda : self.search_dir(self.line_path_templates)) # Buscar la carpeta de las plantillas
        self.bt_select_notebook.clicked.connect(lambda : self.search_file(self.notebook_line))
        self.bt_template.clicked.connect(lambda : self.search_file(self.template_line))
        self.bt_close.clicked.connect(lambda : self.close())


    def search_dir(self, line):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select dir')
        line.setText(dir_name) # Escribir la ruta de la carpeta en la linea correspondiente.

    def search_file(self,line):
        file_path = QFileDialog.getOpenFileName(self, 'Select File')
        file_name = file_path[0].split('/')[-1].split('.')[0] # Extraemos solo el nombre del archivo en la ruta.
        line.setText(file_name)
        


if __name__ == '__main__':
	app = QApplication([])
	window = MainApp()
	window.show() #con hide() ocultamos
	app.exec_()
