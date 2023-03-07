'''import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) '''

'''import tkinter'''
'''from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")'''


'''print(dir(tkinter))'''
from random import shuffle


class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()







































