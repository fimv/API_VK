import tkinter as tk
from tkinter import *
from friendsNNGU import calc_age
 
root = tk.Tk()
root.title("Графическая программа на Python")
root.geometry("1200x700")

label1 = Label(text="Введите id или nikname пользователя", fg="#eee", bg="#333")
label1.place(x=20, y=20)
name_entry = Entry(textvariable=id)
name_entry.place(x=250, y=20)
 
btn2 = Button(text="Отправить запрос", background="#555", foreground="#ccc", padx="14", pady="7", font="13", command=calc_age(id))
btn2.place(x=50, y=50)

txt_edit1 = tk.Text(root)#text="text", fg="#eee", bg="#333")
txt_edit1.place(x=20, y=130, width=1150)

#txt_edit0 = Label(text="text", fg="#eee", bg="#333")
#txt_edit0.place(x=20, y=110, width=1150)

text = "ggggggggg" #input_file.read()
text2 = my_list_sorted
txt_edit1.insert(tk.END, text)
txt_edit1.insert(tk.END, text2)

 
root.mainloop()
