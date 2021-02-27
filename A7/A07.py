from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer

class CookieClicker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cookies = 0
        self.cpers = 0.1
        self.cperc = 1
        self.image = QImage('cheese.png')
        self.curcost = 5
        self.bakcost = 25
        self.faccost = 50
        self.curlevel = 1
        self.bakelevel = 1
        self.faclevel = 1

        self.image_view = QLabel()

        self.ctext = QLabel()
        self.stext = QLabel()
        self.clk = QPushButton("&click", self)
        self.cursbtn = QPushButton("&Cursor", self)
        self.bakebtn = QPushButton("&?", self)
        self.facbtn = QPushButton("&?", self)

        self.setupUI()

    def setupUI(self):

        # Add a menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(exit_action)

        # The right part: the tools to product cookies
        right = QFrame()
        rlayout = QVBoxLayout()
        right.setLayout(rlayout)

        self.cursbtn.clicked.connect(self.addCursor)
        rlayout.addWidget(self.cursbtn)

        self.bakebtn.setEnabled(False)
        self.bakebtn.clicked.connect(self.addBakery)
        rlayout.addWidget(self.bakebtn)

        self.facbtn.setEnabled(False)
        self.facbtn.clicked.connect(self.addFactory)
        rlayout.addWidget(self.facbtn)

        # The body
        main = QFrame()
        mlayout = QHBoxLayout()
        main.setLayout(mlayout)

        self.clk.clicked.connect(self.addcookie)
        mlayout.addWidget(self.clk)

        # main Image
        self.image_view.setPixmap(QPixmap(self.image))
        mlayout.addWidget(self.image_view)

        mlayout.addWidget(right)

        banner = QFrame()
        blayout = QHBoxLayout()
        banner.setLayout(blayout)

        self.ctext.setText("Cookies: " + str(self.cookies))
        blayout.addWidget(self.ctext)

        self.stext.setText("Cookies per second: " + str(self.cpers))
        blayout.addWidget(self.stext)

        self.frame = QFrame()
        layout = QVBoxLayout()
        self.frame.setLayout(layout)
        layout.addWidget(banner)
        layout.addWidget(main)

        self.setCentralWidget(self.frame)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(100)

    def addCursor(self):
        if self.cookies > self.curcost:
            self.curlevel += 1
            self.curcost *= 1.2
            self.cookies -= self.curcost
            self.cpers += 0.2

    def addBakery(self):
        if self.cookies > self.bakcost:
            self.bakelevel += 1
            self.bakcost *= 1.2
            self.cookies -= self.bakcost
            self.cpers += 2

    def addFactory(self):
        if self.cookies > self.faccost:
            self.faclevel += 1
            self.faccost *= 1.2
            self.cookies -= self.faccost
            self.cpers += 20

    def addcookie(self):
        self.cookies += self.cperc

    def updateGame(self):
        self.cookies += 0.1 * self.cpers
        if self.curlevel >= 5:
            self.bakebtn.setEnabled(True)
            self.bakebtn.setText("{} {:.1f}".format("&Bakery", self.bakcost))
        if self.bakelevel >= 5:
            self.facbtn.setEnabled(True)
            self.facbtn.setText("{} {:.1f}".format("&Factory", self.faccost))
        self.ctext.setText("{}{:.1f}".format("Cookies: ", self.cookies))
        self.stext.setText("{}{:.1f}".format("Cookies per second: ", self.cpers))
        self.cursbtn.setText("{} {:.1f}".format("&Cursor", self.curcost))
        # self.bakebtn.setText("{} {:.1f}".format("&Bakery", self.bakcost))
        # self.facbtn.setText("{} {:.1f}".format("&Factory", self.faccost))

    # Quit the program by telling Qt to quit the application
    def quit_program(self):
        qApp.quit()


if __name__ == '__main__':
    app = QApplication([])
    window = CookieClicker()
    window.show()
    app.exec_()
