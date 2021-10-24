# import os
# import tkinter as tk
# import tkinter.ttk as ttk
# import pygubu
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import random

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "Gambler.ui")
#
# class GamblerApp:
#     def __init__(self, master=None):
#         self.builder = builder = pygubu.Builder()
#         builder.add_resource_path(PROJECT_PATH)
#         builder.add_from_file(PROJECT_UI)
#         self.mainwindow = builder.get_object('toplevel1', master)
#
#         self.fund = None
#         self.casino_fund = None
#         self.bet = None
#         self.winning_prob = None
#         builder.import_variables(self, ['fund', 'casino_fund', 'bet', 'winning_prob'])
#
#         builder.connect_callbacks(self)
#
        # self.fund1 = self.fund.get()
        # self.casino_fund1 = self.casino_fund.get()
        # self.bet1 = self.bet.get()
        # self.winning_prob1 = self.winning_prob.get()
        # self.win_con = self.fund.get() + self.casino_fund.get()
#
    # X = []
    # Y = []
    # count = 0
#
#
# def run_simulation(self, frame):
#     List = [0, 1]
#
#     self.fund1 = self.fund.get()
#     self.casino_fund1 = self.casino_fund.get()
#     self.bet1 = self.bet.get()
#     self.winning_prob1 = self.winning_prob.get()
#     self.win_con = self.fund.get() + self.casino_fund.get()
#
#     if self.fund1 > 0 and self.fund1 < self.win_con:
#         result = random.choices(List, weights=[100 - self.winning_prob1, self.winning_prob1], k=1)
#         self.count += 1
#
#         if result[0] == 1:
#             self.fund1 = self.fund1 + self.bet1
#             self.casino_fund1 = self.casino_fund1 - self.bet1
#         else:
#             self.fund1 -= self.bet1
#             self.casino_fund1 += self.bet1
#
#         self.X.append(self.count)
#         self.Y.append(self.fund1)
#     plt.plot(self.X, self.Y)
#
#
# def Graph(self):
#     plt.style.use('fivethirtyeight')
#     print("titan")
#     ani = FuncAnimation(plt.gcf(), self.run_simulation, interval=100)
#     plt.tight_layout()
#     plt.show()
#
#     def run(self):
#         self.mainwindow.mainloop()
#
#
# if __name__ == '__main__':
#     app = GamblerApp()
#     app.run()
#

import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "Gambler.ui")


class GamblerApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.label1 = ttk.Label(self.toplevel1)
        self.label1.configure(compound='top', cursor='based_arrow_down', style='Toolbutton', text='Initial budget:')
        self.label1.place(anchor='nw', relx='0.1', rely='0.10', x='0', y='0')
        self.scale1 = ttk.Scale(self.toplevel1)
        self.fund = tk.IntVar(value=10)
        self.scale1.configure(from_='10', orient='horizontal', state='normal', to='500')
        self.scale1.configure(value='10', variable=self.fund)
        self.scale1.place(anchor='nw', relx='0.36', rely='0.10', width='300', y='0')
        self.scale1.configure(command=self.fund_update)
        self.label2 = ttk.Label(self.toplevel1)
        self.label2.configure(text='Casino fund')
        self.label2.place(anchor='nw', relx='0.1', rely='0.3', x='0', y='0')
        self.scale3 = ttk.Scale(self.toplevel1)
        self.casino_fund = tk.IntVar(value=10)
        self.scale3.configure(from_='10', orient='horizontal', state='normal', to='500')
        self.scale3.configure(value='10', variable=self.casino_fund)
        self.scale3.place(anchor='nw', relx='0.36', rely='0.3', width='300', x='0', y='0')
        self.scale3.configure(command=self.casino_fund_update)
        self.label3 = ttk.Label(self.toplevel1)
        self.label3.configure(text='Bet')
        self.label3.place(anchor='nw', relx='0.1', rely='0.7', x='0', y='0')
        self.entry1 = ttk.Entry(self.toplevel1)
        self.bet = tk.StringVar(value='1')
        self.entry1.configure(font='TkDefaultFont', justify='right', style='Toolbutton', textvariable=self.bet)
        self.entry1.configure(validate='none', width='5')
        _text_ = '''1'''
        self.entry1.delete('0', 'end')
        self.entry1.insert('0', _text_)
        self.entry1.place(anchor='nw', relx='0.36', rely='0.7', x='0', y='0')
        self.label4 = ttk.Label(self.toplevel1)
        self.label4.configure(text='Player wining probability')
        self.label4.place(anchor='nw', relx='0.1', rely='0.5', x='0', y='0')
        self.scale6 = ttk.Scale(self.toplevel1)
        self.winning_prob = tk.IntVar(value=50)
        self.scale6.configure(from_='1', orient='horizontal', state='normal', to='100')
        self.scale6.configure(value='50', variable=self.winning_prob)
        self.scale6.place(anchor='nw', relx='0.36', rely='0.5', width='300', x='0', y='0')
        self.scale6.configure(command=self.winning_prob_update)
        self.button1 = ttk.Button(self.toplevel1)
        self.button1.configure(default='normal', text='Play!')
        self.button1.place(anchor='nw', relx='0.48', rely='0.8', x='0', y='0')
        self.button1.configure(command=self.Graph)
        self.Fund_Val = ttk.Label(self.toplevel1)
        self.Fund_Val.configure(text='10')
        self.Fund_Val.place(anchor='nw', relx='0.9', rely='0.10', x='0', y='0')
        self.Casino_Val = ttk.Label(self.toplevel1)
        self.Casino_Val.configure(text='10')
        self.Casino_Val.place(anchor='nw', relx='0.9', rely='0.30', x='0', y='0')
        self.WinProb_val = ttk.Label(self.toplevel1)
        self.WinProb_val.configure(takefocus=True, text='50')
        self.WinProb_val.place(anchor='nw', relx='0.9', rely='0.50', x='0', y='0')
        self.toplevel1.configure(height='200', relief='raised', takefocus=True, width='600')

        # Main widget
        self.mainwindow = self.toplevel1

        self.fund1 = 10
        self.casino_fund1 = 10
        self.bet1 = 1
        self.winning_prob1 = 50
        self.win_con = self.fund1 + self.casino_fund1

    def fund_update(self, scale_value):
        self.Fund_Val.configure(text =str(int(float(scale_value))))
        self.fund1 = int(float(scale_value))
        self.win_con = self.fund1 + self.casino_fund1


    def casino_fund_update(self, scale_value):
        self.Casino_Val.configure(text = str (int(float(scale_value))))
        self.casino_fund1 = int(float(scale_value))
        self.win_con = self.fund1 + self.casino_fund1


    def winning_prob_update(self, scale_value):
        self.WinProb_val.configure(text = str(int(float(scale_value))))
        self.winning_prob1 = int(float(scale_value))

    X = []
    Y = []
    count = 0

    def run_simulation(self, frame):
        self.bet1 = int(self.bet.get())
        List = [0, 1]

        if self.fund1 > 0 and self.fund1 < self.win_con:
            result = random.choices(List, weights=[100 - self.winning_prob1, self.winning_prob1], k=1)
            self.count += 1

            if result[0] == 1:
                self.fund1 = self.fund1 + self.bet1
                self.casino_fund1 = self.casino_fund1 - self.bet1
            else:
                self.fund1 -= self.bet1
                self.casino_fund1 += self.bet1

            self.X.append(self.count)
            self.Y.append(self.fund1)
        plt.cla()

        plt.ylabel("player's current budget")
        plt.xlabel('number of turns')

        plt.plot(self.X, self.Y)

    def Graph(self):
        self.X.clear()
        self.Y.clear()
        self.count = 0

        self.X.append (0)
        self.Y.append(self.fund1)


        ani = FuncAnimation(plt.gcf(), self.run_simulation, interval=100)
        plt.tight_layout()
        plt.show()

        ani.frame_seq = ani.new_frame_seq()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = GamblerApp()
    app.run()


