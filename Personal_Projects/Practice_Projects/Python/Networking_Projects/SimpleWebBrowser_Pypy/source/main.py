from PyQt5.QtWidgets import *
# from PyQt5.QtGui import * #   not used
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


# class MyWebBrowser(QMainWindow):
#     def __init__(self, *args, **kwargs):
        # super(MyWebBrowser, self).__init__(*args, **kwargs)

class MyWebBrowser():
    """Turns out that inheritance was not needed"""
    def __init__(self, *args, **kwargs):
        self.window = QWidget()
        self.window.setWindowTitle("Evenhaazer Web Browser")

        #   A vertical box layout
        self.layout = QVBoxLayout()
        #   horizontal box
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        #   Gets the text from the url bar and pass it to the `navigate` function
        #   connect just runs the function passed into it when the button is clicked
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url:str):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        
        self.browser.setUrl(QUrl(url))



def main():
    app = QApplication([])
    window = MyWebBrowser()
    app.exec_()


if __name__ == "__main__":
    main()
        
