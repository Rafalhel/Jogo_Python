import PyQt5.QtWidgets as pq
from random import randint

app = pq.QApplication([])
mainwindow = pq.QMainWindow()
mainwindow.setGeometry(500,100,400,300)

#Botão
bt_p = pq.QPushButton(mainwindow)
bt_p.setGeometry(145,240,100,30)
bt_p.setText("Próximo")

btn = pq.QPushButton(mainwindow)
btn.setGeometry(145,240,100,30)
btn.setText("Adivinhar")
btn.setVisible(False)

#Caixa de textos
lb = pq.QLineEdit(mainwindow)
lb.setGeometry(15,90,160,25)

lbb = pq.QLineEdit(mainwindow)
lbb.setGeometry(210,90,160,25)

lba = pq.QLineEdit(mainwindow)
lba.setGeometry(15,90,160,25)
lba.setVisible(False)

lbba = pq.QLineEdit(mainwindow)
lbba.setGeometry(210,90,160,25)
lbba.setVisible(False)

#Labels
result = pq.QLabel(mainwindow)
result.setGeometry(190,90,12,25)
result.setText("")

lbl = pq.QLabel(mainwindow)
lbl.setGeometry(15,30,1000,25)
lbl.setText("Olá, player 1, qual é o seu nome ?")

lbla = pq.QLabel(mainwindow)
lbla.setGeometry(25,140,1000,30)
lbla.setText("O Objetivo do jogo é adivinhar um número aleátorio entre 0 e 10\n")

lbl2 = pq.QLabel(mainwindow)
lbl2.setGeometry(15,160,1000,25)
lbl2.setText("")

lblp = pq.QLabel(mainwindow)
lblp.setGeometry(15,130,1000,25)
lblp.setText("")


lbll = pq.QLabel(mainwindow)
lbll.setGeometry(210,30,1000,25)
lbll.setText("Olá, player 2, qual é o seu nome ?")

lbll2 = pq.QLabel(mainwindow)
lbll2.setGeometry(210,160,1000,25)
lbll2.setText("")

lbllp = pq.QLabel(mainwindow)
lbllp.setGeometry(210,130,1000,25)
lbllp.setText("")

lz = pq.QLabel(mainwindow)
lz.setGeometry(15,165,1000,25)
lz.setText("")

lz2  = pq.QLabel(mainwindow)
lz2.setGeometry(210,165,1000,25)
lz2.setText("")


i = lb.text()#input("Olá, player 1, qual é o seu nome?\n")
p = lbb.text()#("Olá, player 2, qual é o seu nome?\n")
score1 = 0
score2 = 0
def sumir(self):
    bt_p.setVisible(False)
    btn.setVisible(True)
    if lb.text() == "":
        lb.setText("P1")
    if lbb.text() == "":
        lbb.setText("P2")
    lbl.setText(lb.text() + ", digite um número: ")
    lbll.setText(lbb.text() + ", digite um número")
    lz.setText("Score: 0")
    lz2.setText("Score: 0")
    lb.setVisible(False)
    lbb.setVisible(False)
    lba.setVisible(True)
    lbba.setVisible(True)
    lbla.setVisible(False)

def adivinhar(self):
    global score1
    global score2
    z = str(randint(0, 10))
    x = lba.text()
    y = lbba.text()
    if z != x:
        lblp.setText("Errou")
        lba.clear()
    elif z == x:
        lblp.setText("Acertou")
        score1 += 1
        lz.setText("Score: " + str(score1))
        int(score1)
        lba.clear()
    if z != y:
        lbllp.setText("Errou")
        lbba.clear()
    elif z == y:
        lbllp.setText("Acertou")
        score2 += 1
        lz2.setText("Score: " + str(score2))
        int(score2)
        lbba.clear()
    result.setText(z)

bt_p.clicked.connect(sumir)
btn.clicked.connect(adivinhar)

mainwindow.show()
app.exec_()