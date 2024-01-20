from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('TIC TAC')
root.iconbitmap()
root.resizable(False, False)
#root.geometry("1200x710")

# X starts so true
clicked = True
count = 0

# Reset the game


# disable buttons
def disableButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check for win status
def checkWin():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":   # 1st row
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()
    
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X": # 2nd row
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X": # 3rd row
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X": # 1st column
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X": # 2nd column
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X": # 3rd column
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X": # top to bottom diagonal
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    elif b7["text"] == "X" and b5["text"] == "X" and b3["text"] == "X": # bottom to top diagonal
        b7.config(bg="green")
        b5.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player win!")
        disableButtons()

    
    # CHECK IF O WINS
        
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":   # 1st row
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O": # 2nd row
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O": # 3rd row
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O": # 1st column
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O": # 2nd column
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O": # 3rd column
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O": # top to bottom diagonal
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()

    elif b7["text"] == "O" and b5["text"] == "O" and b3["text"] == "O": # bottom to top diagonal
        b7.config(bg="green")
        b5.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Computer win!")
        disableButtons()
    
    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Game draw!")
        disableButtons() 

# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkWin()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkWin()
    else: 
        messagebox.showerror("Tic Tac Toe", "Bad input")

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), 
                height=3, width=6, bg="silver", 
                command=lambda: b_click(b9))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# Create a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Create options menu
optionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Reset game", command=reset)
reset()
root.mainloop()