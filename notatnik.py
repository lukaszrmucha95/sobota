import tkinter as tk
root = tk.Tk()
root.title("notatnik")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
plik_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Plik", menu=plik_menu)
plik_menu.add_command(label="Nowa Karta")
plik_menu.add_command(label="Nowe Okno")
plik_menu.add_command(label="Zapisz")
plik_menu.add_command(label="Zapisz jako")

root.mainloop()
