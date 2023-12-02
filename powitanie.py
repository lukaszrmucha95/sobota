from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("350x350")
root.title("Przykład z messagebox")

def pokaz_komunikat():
    imie = entry.get()

    if imie.isalpha():
        messagebox.showinfo("Witaj!", f"Witaj {imie}!")
    else:
        messagebox.showerror("Bład", "Prosze wpisac poprawne imie (wyłącznie litery; bez cyfr)")

label = Label(root, text="Wpisz swoje imie:")
label.pack(pady=12)

entry = Entry(root)
entry.pack(pady=12)
button = Button(root, text="ok", command=pokaz_komunikat)
button.pack(pady=5)

root.mainloop()
