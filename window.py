from tkinter import *
from tkinter import ttk
import map_gen

root = Tk()
root.title("Map Proof-of-Concept")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mapdraw = StringVar()
mapdraw.set = map_gen.map_proof()
mapgen = ttk.Label(mainframe, mapdraw)

root.mainloop()