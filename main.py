# ch 4.2.3 main.py
import sys # 시스템 제어 관련 모듈 

# 위젯이란 : GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import QIcon

# 나는 계산기 유형을 직접 정의한다! 이때, QWidget에 기반을 둔다
class Calculator(QWidget) :

    def initUI(self) :

        self.te1 = QPlainTextEdit()
        self.te1 = setReadOnly(True)
        self.btn1 = QPushButton('Message', self)

        # 이벤트 핸들링 : 클릭했을 때, 뭐를 할거다! 라고 정하는 것.
        self.btn1.clicked.connect(self.activateMessage)
        
        vbox = QVBoxLayout()
        vbox.addwidget(self.te1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

    def activateMessage(self) : 
        self.te1.appenPlainText("Button clicked!")