from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import sys
import os

root = Tk()
root.title('TIC TAC TOE')
root.resizable(False, False)

path = os.path.join(sys.path[0], "Assets/zim.png")
icon = Image.open(path)
icon = icon.resize((32, 32))  
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)


def center_window(window):
    window_width = 500  
    window_height = 400  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

clicked = True
count = 0

def disableButtons():
    for button in buttons:
        button.config(state=DISABLED)

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]
]

def checkWin():
    global winner
    winner = False
    for combination in winning_combinations:
        if all(buttons[i]["text"] == "X" for i in combination):
            for i in combination:
                buttons[i].config(bg="#80FF80")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player win!")
            disableButtons()
            break
        elif all(buttons[i]["text"] == "O" for i in combination):
            for i in combination:
                buttons[i].config(bg="#80FF80")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Computer win!")
            disableButtons()
            break
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        disableButtons()

def checkPlayerWin():
    for combination in winning_combinations:
        if all(buttons[i]["text"] == "X" for i in combination):
            return True
    if count == 9 and not winner:
        return False

def checkComputerWin():
    for combination in winning_combinations:
        if all(buttons[i]["text"] == "O" for i in combination): 
            return True
    if count == 9 and not winner:
        return False

def compMove():
    global count
    available_spots = [i for i in range(len(buttons)) if buttons[i]["text"] == " "]
    if available_spots:
        entryFlag = True
        if(entryFlag == True):
            for i in available_spots:
                buttons[i]["text"] = "O"
                buttons[i].config(fg="#ed5555")
                if (checkComputerWin()):
                    entryFlag = False
                    count += 1
                    break
                else:
                    buttons[i]["text"] = " "
                    buttons[i].config(fg="#ffca4f")
        if(entryFlag == True):
            for i in available_spots:
                buttons[i]["text"] = "X"
                if (checkPlayerWin()):
                    entryFlag = False
                    buttons[i]["text"] = "O"
                    buttons[i].config(fg="#ed5555")
                    count += 1
                    break
                else:
                    buttons[i]["text"] = " "
                    buttons[i].config(fg="#ffca4f")
        if(entryFlag == True):
            entryFlag = False
            random_index = random.choice(available_spots)
            buttons[random_index]["text"] = "O"
            buttons[random_index].config(fg="#ed5555")
            count += 1

def b_click(b):
    global count
    if (b["text"] == " ") and (count%2==0):
        b["text"] = "X"
        count += 1
        checkWin()
        if not checkPlayerWin():
            compMove()
        if (checkComputerWin() and not checkPlayerWin()):
            checkWin()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box...")

def reset():
    global clicked, count
    clicked = True
    count = 0
    for button in buttons:
        button.config(text=" ", bg="#343638", state=NORMAL)

buttons = [Button(root, text=" ", font=("Nevis", 30, "bold"), width=8, fg="#ffca4f", cursor="hand2", activebackground="#81a0a6", command=lambda x=i: b_click(buttons[x])) for i in range(9)]

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)

for i in range(3):
    for j in range(3):
        buttons[i*3 + j].config(bg='#343638')
        buttons[i*3 + j].grid(row=i, column=j, sticky='nsew')

myMenu = Menu(root, font=('Arial', 13))
root.config(menu=myMenu)

optionMenu = Menu(myMenu, tearoff=False, font=('Arial', 13))
myMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Reset Game", command=reset)

center_window(root)
root.mainloop()
