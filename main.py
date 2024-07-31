import os
import sys
from time import sleep, time, strftime, gmtime
from datetime import date, datetime
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.uic import loadUi

rute = Path(os.path.abspath(__file__)).parent
sys.path.append(str(rute))

from gui.create_notebook import Ui_create_book
from gui.session import Ui_session
from source import functions as sf

# Rutas
# folder = Path('/home/dracul/programing/python/guis/generador_notas/')
config = sf.load_yaml('config.yaml')
TEMPLATES = Path(config['templates'])
NOTEBOOKS = Path(config['notebooks'])
HOME = Path(config['home'])

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp,self).__init__()
        self.setFixedSize(1000,500)
        self.setWindowTitle('N_gen')
        loadUi('gui/main.ui',self)
        # Default values
        self.line_path_templates.setText(str(TEMPLATES / 'session_normal.yaml'))
        self.line_path_notes.setText(str(NOTEBOOKS))
        # Buttons signals
        self.bt_search_notes.clicked.connect(lambda : self.search_dir(self.line_path_notes)) # Buscar la carpeta del cuaderno
        self.bt_search_templates.clicked.connect(lambda : self.search_file(self.line_path_templates,'full')) # Buscar la carpeta de las plantillas
        self.bt_select_notebook.clicked.connect(lambda : self.search_file(self.notebook_line))
        self.bt_close.clicked.connect(lambda : self.close())

        self.bt_create.clicked.connect(self.create_window)
        self.bt_session.clicked.connect(self.session_window)

    def search_dir(self, line):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select dir',str(HOME))
        line.setText(dir_name) # Escribir la ruta de la carpeta en la linea correspondiente.

    def search_file(self,line, mode='short'):
        file_path = QFileDialog.getOpenFileName(self, 'Select File', str(HOME))
        match mode:
            case 'short':
                file_name = file_path[0].split('/')[-1].split('.')[0] # Extraemos solo el nombre del archivo en la ruta.
                line.setText(file_name)
            case 'full':
                line.setText(file_path[0])
            case _:
                pass

    def create_window(self):
        self.c_window = CreateNotebook()
        self.c_window.show()


    def session_window(self):
        if self.line_path_templates.text() == '' or self.line_path_notes.text() == '' or self.notebook_line.text() == '':
            # To blink
            self.line_path_templates.setStyleSheet('background-color: red')
            self.line_path_notes.setStyleSheet('background-color: red')
            self.notebook_line.setStyleSheet('background-color: red')
        else:
            file_path = Path(self.line_path_templates.text())
            parent = file_path.parent
            file_name = file_path.name.split('.')[0]
            context = {
                'fecha': date.today().__format__('%d-%m-%Y'),
                'hora': datetime.now().__format__('%H:%M'),
                'title': self.session_line.text()
                       }
            session_content = sf.read_template(parent,file_name, context)
            note_path = Path(self.line_path_notes.text())
            note_path = note_path / f'{self.notebook_line.text()}.md'
            sf.write_in_note_book(note_path, session_content)
            self.s_window = Session(note_path)
            self.s_window.show()

class CreateNotebook(QMainWindow):
    def __init__(self):
        super(CreateNotebook,self).__init__()
        self.setFixedSize(800,300)
        self.setWindowTitle('New_notebook')
        self.ui =  Ui_create_book()
        self.ui.setupUi(self)

        # Buttons
        self.ui.bt_close.setIcon(QIcon('gui/images/Cerrar.svg'))

        # ------------------------- Signals -------------------------
        self.ui.bt_close.clicked.connect(lambda : self.close())
        self.ui.bt_search.clicked.connect(lambda : self.search_dir(self.ui.line_path))
        self.ui.bt_create.clicked.connect(self.create_nb)

    #------------- Slots -------------------
    def create_nb(self):
        if self.ui.line_name.text() == '':
            self.ui.line_name.setStyleSheet('background-color: red;')
        elif self.ui.line_path.text() == '':
            self.ui.line_path.setStyleSheet('background-color: red;')
        else:
            self.ui.line_name.setStyleSheet('background-color: green;')
            self.ui.line_path.setStyleSheet('background-color: green;')
            today = date.today().__format__('%d-%m-%Y')
            context = {
                'fecha' : today,
                'hora' : datetime.now().__format__('%H:%M'),
                'tema' : self.ui.line_teme.text()
            }
            sf.render_template(TEMPLATES,
                               'cuaderno',
                               NOTEBOOKS / f'{self.ui.line_name.text()}.md',
                               context)
            sleep(1)
            self.close()

    def search_dir(self, line):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select dir')
        line.setText(dir_name) # Escribir la ruta de la carpeta en la linea correspondiente.

class Session(QMainWindow):
    def __init__(self, note_path):
        super(Session,self).__init__()
        self.note_path = note_path
        self.setFixedSize(800,300)
        self.setWindowTitle('session_name')
        self.ui = Ui_session()
        self.ui.setupUi(self)
        self.start_time = time()

        self.ui.bt_close.setIcon(QIcon('gui/images/Cerrar.svg'))
        self.ui.bt_send.setShortcut('Ctrl+S')
        # self.ui.bt_send.setShortcut(Qt.CTRL + Qt.Key_S)

        # Signals

        self.ui.bt_close.clicked.connect(self.close_session)
        self.ui.bt_send.clicked.connect(self.send_text)

    #===========================================#
    #                   SLOTS                   #
    #===========================================#

    def send_text(self):
        text = self.ui.sesion_text.toPlainText()
        if text != '':
            text = text + f' ({strftime("%H:%M:%S",gmtime(time()-self.start_time))})'
            sf.write_in_note_book(self.note_path,text)
            self.ui.sesion_text.setPlainText('')
        else:
            pass


    def close_session(self):
        sf.write_in_note_book(self.note_path,f'\n**Final** --> {datetime.now().__format__('%H:%M')}')
        self.close()

if __name__ == '__main__':
	app = QApplication([])
	window = MainApp()
	# c_window = CreateNotebook()
	window.show() #con hide() ocultamos
	app.exec_()
