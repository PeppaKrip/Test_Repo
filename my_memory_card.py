#создай приложение для запоминания информации
# | вертикально(V)
# - горизонтально(H)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Memory Card')
AnswerBox = QGroupBox('|||||')
questionBox=QGroupBox('Варианты')
questionInApp = QLabel('Какой национальности не существует?')
ansResult = QLabel('Правильно/Неправильно')
right_answer = QLabel('Правильный ответ')
AnswerBox.hide()
main_window.score = 0
main_window.total = 0


class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

pushbttn = QPushButton('Ответить')
bttn1 = QRadioButton('Энцы')
bttn2 = QRadioButton('Смурфы')
bttn3 = QRadioButton('Чулымцы')
bttn4 = QRadioButton('Алеуты')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(bttn1)
ButtonGroup.addButton(bttn2)
ButtonGroup.addButton(bttn3)
ButtonGroup.addButton(bttn4)


answers = [bttn1, bttn2, bttn3, bttn4]

v_layout = QVBoxLayout()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()
h_layout3 = QHBoxLayout()

v_layoutAnsBox = QVBoxLayout()
h_layoutBox = QHBoxLayout()
v_layout1Box = QVBoxLayout()
v_layout2Box = QVBoxLayout()


def show_question():
    ButtonGroup.setExclusive(False)
    bttn1.setChecked(False)
    bttn2.setChecked(False)
    bttn3.setChecked(False)
    bttn4.setChecked(False)
    ButtonGroup.setExclusive(True)
    questionBox.show()
    AnswerBox.hide()
    pushbttn.setText('Ответить')

def show_correct(a):
    ansResult.setText(a)
    show_result()

def check_ans():
    if answers[0].isChecked():
        show_correct("Правильно")
        main_window.score += 1
        print('Правильных ответов: ', main_window.score)
        print(main_window.score/(main_window.total)*100)
    elif answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
        print(main_window.score/(main_window.total)*100)
        show_correct('Неправильно')
    
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    questionInApp.setText(q.question)
    right_answer.setText(q.right_ans)
    show_question()

question_list = []
q1 = Question('Дочерняя студия EA, создавшая Titanfall','Respawn Entertainment', 'Orb Inc', 'Blizzard', 'Dice')
q2 = Question('Когда выйдет Cyberpunk 2077?', '10 декабря', '19 ноября', 'Никогда', 'Его снова отложат')
q3 = Question('2 + 2', '4', '53', '43?', '15!')
q4 = Question("Какая компания выкупила Bethesd'у?", 'Microsoft', 'Xbox', 'Google', 'Apple')
q5 = Question('14-ти нанометровый процесс какой компании опережает по энергоэффективности 7-ми нанометровый процесс Nvidia?', 'Samsung', 'Amd', 'Apple', 'Kingston')
q6 = Question("Кто написал произведение 'Война и мир'?", 'Толстой', 'Тютчев', 'Пушкин', 'Гоголь')
q7 = Question('Официальное название API Directx 12', 'Vulcan', 'OpenGl', 'Tesla', 'Cuda')
q8 = Question('Первая компания, выпустившая видеокарты с поддержкой трассировки лучей в реальном времени', 'Nvidia', 'Amd', 'Intel', 'Huanan')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)

main_window.cur_question = -1

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    d = question_list[cur_question]
    main_window.total += 1
    print('Всего вопросов: ', main_window.total)
    ask(d)
    

def click_ok():
    if pushbttn.text() == 'Ответить':
        check_ans()
    else:
        next_question()

def show_result():
    questionBox.hide()
    AnswerBox.show()
    pushbttn.setText('Следующий вопрос')
    
pushbttn.clicked.connect(click_ok)

v_layoutAnsBox.addWidget(ansResult, alignment = Qt.AlignLeft)
v_layoutAnsBox.addWidget(right_answer, alignment = Qt.AlignCenter)

v_layout1Box.addWidget(bttn1, alignment = Qt.AlignCenter)
v_layout1Box.addWidget(bttn3, alignment = Qt.AlignCenter)
v_layout2Box.addWidget(bttn2, alignment = Qt.AlignCenter)
v_layout2Box.addWidget(bttn4, alignment = Qt.AlignCenter)
h_layoutBox.addLayout(v_layout1Box)
h_layoutBox.addLayout(v_layout2Box)
questionBox.setLayout(h_layoutBox)
AnswerBox.setLayout(v_layoutAnsBox)

h_layout1.addWidget(questionInApp, alignment = Qt.AlignCenter)
h_layout2.addWidget(pushbttn, alignment = Qt.AlignCenter)
h_layout3.addWidget(questionBox)
h_layout3.addWidget(AnswerBox)

v_layout.addLayout(h_layout1)
v_layout.addLayout(h_layout3)
v_layout.addLayout(h_layout2)
next_question()
main_window.setLayout(v_layout)
main_window.show()
app.exec_()
