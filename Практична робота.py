from tkinter import *

def click(event):
  root["bg"] = "red"
  new_y = 200
  new_width = root.winfo_width() + 300
  new_x = root.winfo_x() - 50
  root.geometry(f"{new_width}x100+{new_x}+{new_y}")

root = Tk()
root["bg"] = "gray"
root.geometry("200x100+150+100")
root.title("Практична робота")
root.bind("<1>", click)
