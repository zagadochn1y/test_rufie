from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором распологается приветствие '''
        super().__init__()
        # создаём и настраиваем графические элементы:
        self.initUI()
        # устанавливает свзяи между элементами
        self.connects()
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()
    
    def initUI(self):
        ''' создаёт графичиские элементы '''
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)


    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' устанавливает, как бадет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec()