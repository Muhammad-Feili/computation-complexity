import tkinter as tk
from tkinter import messagebox
from InformalLanguageProject import finiteAutomata
from InformalLanguageProject import dfa

class State(tk.Button):
    def __init__(self,name,label,isFinal=False,isInitial=False):
        super().__init__()
        self.text=label
        self.Name=name
    def changeLabel(self,new_label):
        self.text=new_label
    def changeName(self,new_name):
        self.Name=new_name

class Transition():
    def __init__(self,head_state,label,tail_state):
        self.initial_state=head_state
        self.Label=label
        self.final_state=tail_state
    def setLabel(self,new_label):
        self.Label=new_label

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title='Informal Language'

        def StateButton():
            tk.messagebox.showinfo(title='SayHello',message='علی اصغر')

        stateButton=tk.Button(self,height=2,width=5,text='State',command=StateButton)
        stateButton.place(x=50,y=50)

        def state():
            messagebox.showwarning(title='hello',message='hello my friend!')

        state=State('S0','start',True,True)
        state.config(height=2,width=5,command=state)
        state.place(x=100,y=100)

        transitionButton=tk.Button(self,height=2,width=5,text='Transition')
        transitionButton.place(x=150,y=150)

if __name__=='__main__':
    window=Window()
    window.mainloop()