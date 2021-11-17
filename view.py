from tkinter import *
from tkinter import ttk

import onlinereader

c = onlinereader.read()


def calc_kw(d, h):
    return (
        dict() if c[h][d] == 0
        else dict(background='red') if c[h][d] < 900
        else dict(background='red2') if c[h][d] < 1800
        else dict(background='red3') if c[h][d] < 2700
        else dict(background='red4')
    )


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Dom").grid(column=0, row=0)
ttk.Label(frm, text="Seg").grid(column=1, row=0)
ttk.Label(frm, text="Ter").grid(column=2, row=0)
ttk.Label(frm, text="Qua").grid(column=3, row=0)
ttk.Label(frm, text="Qui").grid(column=4, row=0)
ttk.Label(frm, text="Sex").grid(column=5, row=0)
ttk.Label(frm, text="Sáb").grid(column=6, row=0)
for h in range(24):
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(0, h)).grid(column=0, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(1, h)).grid(column=1, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(2, h)).grid(column=2, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(3, h)).grid(column=3, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(4, h)).grid(column=4, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(5, h)).grid(column=5, row=h+1)
    ttk.Label(frm, text=f"{h:02}:00", **calc_kw(6, h)).grid(column=6, row=h+1)
root.mainloop()
