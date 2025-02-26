from tkinter import *

def click(event):
  root["bg"] = "red"

root = Tk()
root["bg"] = "gray"
root.geometry("200x100 + 150 + 100")
root.title("Практична робота")
root.bind("<1>", click)
