import sys # вызов главной функции
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): # главный класс приложения
    def __init__(self):
        super().__init__() # родительский класс

        self.setWindowTitle("stydia") # название приложения
        self.resize(600, 400) # размеры приложения width, height

        main_widget = QWidget() # центральный виджет который содержит всё
        self.setCentralWidget(main_widget) # выравнивание этого виджета по середине и передаем сам виджет который хотим выравнить

        self.layout_main = QVBoxLayout()

        self.vert_widget = QWidget()
        self.layout_h_main = QHBoxLayout()
        """
        QVBoxLayout() - создаёт макет для вертикального расположения виджетов
        Виды макетов:
        - QVBoxLayout: вертикальное расположение (сверху вниз)
        - QHBoxLayout: горизонтальное расположение (слева направо)  
        - QGridLayout: расположение в сетке (строка/столбец)
        - QFormLayout: для форм (метка + поле ввода)
        """

        


        self.label_card1 = QLabel("Epta1")
        self.label_card1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_card2 = QLabel("Epta2")
        self.label_card2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_card3 = QLabel("Epta3")
        self.label_card3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        """
        .setAlignment(alignment) - устанавливает выравнивание текста внутри метки
        Аргумент: константа из Qt.AlignmentFlag
        
        Возможные значения:
        - Qt.AlignmentFlag.AlignLeft: выравнивание по левому краю
        - Qt.AlignmentFlag.AlignRight: по правому краю  
        - Qt.AlignmentFlag.AlignCenter: по центру
        - Qt.AlignmentFlag.AlignTop: по верху
        - Qt.AlignmentFlag.AlignBottom: по низу
        Можно комбинировать: Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop
        """

        self.button1 = QPushButton("жми на меня")

        self.button2 = QPushButton("not click me")

        self.create_card()
        

        self.layout_h_main.addWidget(self.widget_card)
        self.layout_h_main.addWidget(self.label_card2)
        self.layout_h_main.addWidget(self.label_card3)


        self.widget_card.setLayout(self.layout_widget)

        self.vert_widget.setLayout(self.layout_h_main)


        self.layout_main.addWidget(self.vert_widget)

        self.layout_main.addWidget(self.button2)

        
        main_widget.setLayout(self.layout_main)

        self.button1.clicked.connect(self.on_but1_click)
        self.button2.clicked.connect(self.on_but2_click)

    


    def create_card(self):
        self.widget_card = QWidget()
        self.layout_widget = QVBoxLayout()

        self.layout_widget.addWidget(self.label_card1)
        self.layout_widget.addWidget(self.button1)


    
    def on_but1_click(self):
        self.label_card1.setText("on the click")

    def on_but2_click(self):
        self.label_card2.setText("on the click button 2")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())