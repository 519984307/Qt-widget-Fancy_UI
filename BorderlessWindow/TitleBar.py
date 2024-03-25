from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QWidget


class TitleBarUI:
    def setupUi(self, parent: QWidget):
        parent.setFixedHeight(28)

        self.horizontalLayout = QHBoxLayout(parent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)

        self.title_label = QLabel(text="标题", parent=parent)
        self.horizontalLayout.addWidget(self.title_label)

        self.horizontalSpacer = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.mini_button = QPushButton(text="🗕", parent=parent)
        self.horizontalLayout.addWidget(self.mini_button)

        self.max_button = QPushButton(text="🗖", parent=parent)
        self.horizontalLayout.addWidget(self.max_button)

        self.close_button = QPushButton(text="🗙", parent=parent)
        self.horizontalLayout.addWidget(self.close_button)

        self.mini_button.setFixedSize(35, 20)
        self.max_button.setFixedSize(35, 20)
        self.close_button.setFixedSize(35, 20)

        self.mini_button.setStyleSheet("QPushButton {"
                                       "    color: white;"
                                       "    border: none;"
                                       "    background-color: rgba(0,0,0,0); "
                                       "    border-radius: 5px"
                                       "}"
                                       "QPushButton:hover {"
                                       "    background-color: rgba(229,234,239,50);"
                                       "}")

        self.max_button.setStyleSheet("QPushButton {"
                                      "    color: white;"
                                      "    border: none;"
                                      "    background-color: rgba(0,0,0,0); "
                                      "    border-radius: 5px"
                                      "}"
                                      "QPushButton:hover {"
                                      "    background-color: rgba(229,234,239,50);"
                                      "}")

        self.close_button.setStyleSheet("QPushButton {"
                                        "    color: white;"
                                        "    border: none;"
                                        "    background-color: rgba(0,0,0,0); "
                                        "    border-radius: 5px"
                                        "}"
                                        "QPushButton:hover {"
                                        "    background-color: rgba(196,43,28,255);"
                                        "}")


class TitleBar(QWidget):
    """标题栏"""
    MoveWindow = Signal()

    def __init__(self, parent):
        super(TitleBar, self).__init__(parent)
        self.ui = TitleBarUI()
        self.ui.setupUi(self)

        self.ui.mini_button.clicked.connect(self.window().showMinimized)
        self.ui.max_button.clicked.connect(self.MaximizeButtonClicked)
        self.ui.close_button.clicked.connect(self.window().close)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(127, 127, 127))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.MoveWindow.emit()
            if self.window().isMaximized():
                self.ui.max_button.setText("🗖")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.MaximizeButtonClicked()

    @Slot()
    def MaximizeButtonClicked(self):
        if not self.window().isMaximized():
            self.window().showMaximized()
            self.ui.max_button.setText("🗗")
        else:
            self.window().showNormal()
            self.ui.max_button.setText("🗖")


