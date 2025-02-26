from tkinter import *
from tkinter.messagebox import *

def click(event):
  root["bg"] = "red"
  click_y = 200
  click_width = root.winfo_width() + 300
  click_x = root.winfo_x() - 50
  root.geometry(f"{click_width}x100+{click_x}+{click_y}")
  showinfo("", "Ми вивчаємо програмування!")

def key_press(event):
  root["bg"] = "blue"
  key_y = root.winfo_y() + 300
  key_width = root.winfo_width() + 200
  root.geometry(f"{key_width}x100+{root.winfo_x()}+{key_y}")

root = Tk()
root["bg"] = "gray"
root.geometry("200x100+150+100")
root.title("Практична робота")
root.bind("<1>", click)
root.bind("<KeyPress>", key_press)
