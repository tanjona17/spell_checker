import tkinter
from tkinter import *
from textblob import TextBlob

def check():
    word = text.get()
    a = TextBlob(word)
    true = str(a.correct())
    
    correct = Label(screen,text="The correct text is:")
    correct.place(x=15, y=180)
    spell.config(text=true)
    
    
    

def main_screen():
    global text
    global screen
    global spell
    
    screen = Tk()
    screen.title("Spelling checker")
    screen.geometry("300x300")
    
    heading = Label(screen, text="Spelling checker", fg="black")
    heading.pack(pady=(50,0))
    
    text = Entry(screen, justify="center", width=40, bg="white")
    text.pack(pady=(10,0))
    text.focus()
    
    Button(screen, text="Check", fg="white", bg="#ff3333", bd=0, width=15, command= check).pack(pady=(11,0)) 
    
    spell = Label(screen)
    spell.place(x=120, y=180)
    screen.mainloop()

main_screen()
