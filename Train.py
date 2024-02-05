from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 868)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(0, 0, 1111, 821))
        self.img1.setText("")
        self.img1.setPixmap(QtGui.QPixmap("background.jpg"))
        self.img1.setScaledContents(True)
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QLabel(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(20, 410, 1071, 331))
        self.img2.setText("")
        self.img2.setPixmap(QtGui.QPixmap("rails.png"))
        self.img2.setScaledContents(True)
        self.img2.setObjectName("img2")
        self.trainLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainLabel.setGeometry(QtCore.QRect(10, 530, 811, 91))
        self.trainLabel.setText("")
        self.trainLabel.setPixmap(QtGui.QPixmap("train.jpg"))
        self.trainLabel.setScaledContents(True)
        self.trainLabel.setObjectName("trainLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 680, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Go pushbutton
        self.pushButton.clicked.connect(self.startAnimation)


        # Create the train animation
        self.animation = QPropertyAnimation(self.trainLabel, b"geometry")
        self.animation.setDuration(3000)  # Set the duration of the animation in milliseconds
        # The self.trainLabel.width() returns the width of the self.trainLabel widget. By prefixing it with a minus sign (-), we are effectively subtracting the widget's width from the x-coordinate.
        self.animation.setStartValue(QRect(-self.trainLabel.width(), self.trainLabel.y(), self.trainLabel.width(), self.trainLabel.height()))#postion
        self.animation.setEndValue(QRect(self.img1.width(), self.trainLabel.y(), self.trainLabel.width(), self.trainLabel.height()))#postion
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.finished.connect(self.animationFinished) # Connect to the finished signal

        # Sound:
        # Get the path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the relative path to the sound file
        sound_file_path = os.path.join(script_dir, "train sound.wav")
        self.sound_file = sound_file_path
        # The code will look for the sound file in the same directory as the script


        self.trainLabel.hide() # Train starts hidden


    def animationFinished(self):
        # Stop the sound when the animation finishes and hide the train
        self.player.stop()
        self.trainLabel.hide()

    def playSound(self):
        # Play sound when the train first appears
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(self.sound_file)))
        self.player.play()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))

    def startAnimation(self):
        # Start the train animation when the button is clicked
        self.trainLabel.show()
        self.animation.start()
        self.playSound()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
