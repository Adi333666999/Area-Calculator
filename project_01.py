from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Area Converter by Aditya Patil")
root.geometry("900x900+150+1")
root.configure(bg = "lightpink")
f = ("Century", 30)
fo = ("Times New Roman", 40,  "bold")

Titlelabel = Label(root, text = "Area Converter", font = fo)
Titlelabel.place(x = 300, y = 10)

Squarelabel = Label(root, text = "Square Feet: ", font = f)
Squarelabel.place(x = 50, y = 100)
SquareEntry = Entry(root, font = f)
SquareEntry.place(x = 350, y = 100)

Acrelabel = Label(root, text = "Acre: ", font = f)
Acrelabel.place(x = 50, y = 200)
AcreLabel = Label(root, text = " ", font = f)
AcreLabel.place(x = 350, y = 200)

def calculate():
    square_feet_text = SquareEntry.get()  

    if not square_feet_text:
        showerror("ERROR", "Square feet cannot be blank...")
    elif not all(char.isdigit() or char == "." for char in square_feet_text):
        showerror("ERROR", "Enter Integer...")
    elif int(square_feet_text) < 0:
        showerror("ERROR", "Square feet cannot be negative...")	
    elif not square_feet_text.isdigit():
        showerror("ERROR", "Enter only digits...")
    else:
        try:
            square_feet = float(square_feet_text)
            acre = square_feet / 43560
            AcreLabel.configure(text=acre)
        except ValueError:
            showerror("ERROR", "Invalid input")
SquareEntry.focus()
Submit = Button(root, text = "Convert", font = f, command = calculate) 
Submit.place(x = 400, y = 300)

Acrelabel = Label(root, text = "Acre: ", font = f)
Acrelabel.place(x = 50, y = 400)
AcreEntry = Entry(root, font = f)
AcreEntry.place(x = 350, y = 400)

Squarelabel = Label(root, text = "Square Feet: ", font = f)
Squarelabel.place(x = 50, y = 500)
SquareLabel = Label(root, text = " ", font = f)
SquareLabel.place(x = 350, y = 500)

def calculate():
    acre_text = AcreEntry.get()  

    if not acre_text:
        showerror("ERROR", "Acre cannot be blank...")
    elif not all(char.isdigit() or char == "." for char in acre_text):
        showerror("ERROR", "Enter Integer...")
    elif int(acre_text) < 0:
        showerror("ERROR", "Acre cannot be negative...")	
    elif not acre_text.isdigit():
        showerror("ERROR", "Enter only digits...")
    else:
        try:
            acre = float(acre_text)
            square_feet = acre * 43560
            SquareLabel.configure(text=square_feet)
        except ValueError:
            showerror("ERROR", "Invalid input")
AcreEntry.focus()

Submit = Button(root, text = "Convert", font = f, command = calculate) 
Submit.place(x = 400, y = 600)


root.mainloop()