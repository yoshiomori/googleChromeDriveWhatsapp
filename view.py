import tkinter
from tkinter import ttk

import onlinereader

c = onlinereader.read('last7days')


def calc_kw(d, h):
    if c[h][d] == 0:
        return dict()
    elif c[h][d] < 900:
        return dict(background='red')
    elif c[h][d] < 1800:
        return dict(background='green')
    elif c[h][d] < 2700:
        return dict(background='cyan')
    else:
        return dict(background='blue')


root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
week_name_list = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
column_count = 0
for week_name in week_name_list:
    ttk.Label(frm, text=week_name).grid(column=column_count, row=0)
    column_count += 1
for hour in range(24):
    column_count = 0
    while column_count < 7:
        ttk.Label(frm, text=f"{hour:02}:00", **calc_kw(column_count, hour)).grid(column=column_count, row=hour+1)
        column_count += 1
root.mainloop()
