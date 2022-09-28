import tkinter
from tkinter import Button, Frame, Tk, ttk

class TicTacToe:

    player = 'Você'

    ##Create Main Window and new frame (layout)
    window = Tk()
    frame = Frame(master=window, width=500, height=600)
    frame.pack(pady=10)

    ## Set title Jogo da Velha
    label_title= ttk.Label(master=frame, text="Jogo da Velha",font=("Arial", 15))
    label_title.pack()

    ## Create new frame to allocate buttons
    frame1= Frame(master=window, borderwidth=2, bg='#dadec3')
    frame1.pack(padx=10,pady=10)

    ## Create new frame and set title to round player
    frame2= Frame(master=window, borderwidth=1, bg='#000000')
    frame2.pack(padx=50,pady=10)
    label_round= ttk.Label(master=frame2, text="Round: " + player,font=("Arial", 20))
    label_round.pack()

    ## Create Buttons
    button1 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button3 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button4 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button2 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button5 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button6 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button7 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button8 = Button(master=frame1, text='', width=10, height=5, bg='white')
    button9 = Button(master=frame1, text='', width=10, height=5, bg='white')

    def __init__(self):
        self.board = []

    def create_board(self):
        self.window.title('Jogo da Velha')
        self.window.geometry('500x600')
        self.window.configure(bg='#3b3b3b')

    def create_tiles(self):
        self.button1.grid(row=0,column=0,padx=5,pady=5)
        self.button2.grid(row=0,column=1,padx=5,pady=5)
        self.button3.grid(row=0,column=2,padx=5,pady=5)
        self.button4.grid(row=1,column=0,padx=5,pady=5)
        self.button5.grid(row=1,column=1,padx=5,pady=5)
        self.button6.grid(row=1,column=2,padx=5,pady=5)
        self.button7.grid(row=2,column=0,padx=5,pady=5)
        self.button8.grid(row=2,column=1,padx=5,pady=5)
        self.button9.grid(row=2,column=2,padx=5,pady=5)

    def start(self):
        self.create_board()
        self.create_tiles()
        self.window.mainloop()

tictactoe = TicTacToe()
tictactoe.start()
