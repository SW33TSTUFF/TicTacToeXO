from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('TIC TAC')
# root.iconbitmap('path_to_icon.ico')  
root.resizable(False, False)

# X starts so true
clicked = True
count = 0

# disable all buttons
def disableButtons():
    for button in buttons:
        button.config(state=DISABLED)

# Check for win status
def checkWin():
    global winner
    winner = False

    winning_combinations = [
        [0, 1, 2],  # 1st row
        [3, 4, 5],  # 2nd row
        [6, 7, 8],  # 3rd row
        [0, 3, 6],  # 1st column
        [1, 4, 7],  # 2nd column
        [2, 5, 8],  # 3rd column
        [0, 4, 8],  # top to bottom diagonal
        [6, 4, 2]   # bottom to top diagonal
    ]

    for combination in winning_combinations:
        if all(buttons[i]["text"] == "X" for i in combination): # Checks for all the combinations directly
            for i in combination:
                buttons[i].config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player win!")
            disableButtons()
            break
        elif all(buttons[i]["text"] == "O" for i in combination):
            for i in combination:
                buttons[i].config(bg="green")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Computer win!")
            disableButtons()
            break

    # Check if tie
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        disableButtons()


player_turn = {"current": "X"}
# Button clicked function
def b_click(b):
    global count
    if b["text"] == " ":
        b["text"] = player_turn["current"]
        player_turn["current"] = "O" if player_turn["current"] == "X" else "X"
        count += 1
        checkWin()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box...")


# Reset the game
def reset():
    global clicked, count
    clicked = True
    count = 0
    for button in buttons:
        button.config(text=" ", bg="silver", state=NORMAL)

# Build our buttons
buttons = [Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda x=i: b_click(buttons[x])) for i in range(9)]

# Grid our buttons to the screen
for i in range(3):
    for j in range(3):
        buttons[i*3 + j].grid(row=i, column=j)

# Create a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Create options menu
optionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Reset Game", command=reset)

root.mainloop()
