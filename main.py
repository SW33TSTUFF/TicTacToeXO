from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('TIC TAC TOE')
# root.iconbitmap('path_to_icon.ico')  
root.resizable(False, False)

# X starts so true
clicked = True
count = 0

# disable all buttons
def disableButtons():
    for button in buttons:
        button.config(state=DISABLED)


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

# Check for win status
def checkWin():
    global winner
    winner = False

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


def checkPlayerWin():
    # global winner
    # winner = False

    for combination in winning_combinations:
        if all(buttons[i]["text"] == "X" for i in combination): # Checks for all the combinations directly
            return True
        
    # Check if tie (Probably repetitive)
    if count == 9 and not winner:
        return False
    
def checkComputerWin():
    # global winner
    # winner = False

    for combination in winning_combinations:
        if all(buttons[i]["text"] == "O" for i in combination): 
            return True
        
    # Check if tie
    if count == 9 and not winner:
        return False

def checkTie():
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        disableButtons()

def compMove():
    global count
    available_spots = [i for i in range(len(buttons)) if buttons[i]["text"] == " "]
    
    if available_spots:
        #print(available_spots)
        #random_index = random.choice(available_spots)
        # Check for spots where the computer can win immediately before the player
        entryFlag = True
        if(entryFlag == True):
            for i in available_spots:
                buttons[i]["text"] = "O"
                if (checkComputerWin()):
                    entryFlag = False
                    count += 1
                    break
                else:
                    buttons[i]["text"] = " " # Leave it as it was before
        
        # if there is no such winning condition for the computer then look for winning conditions for the player
        if(entryFlag == True):
            for i in available_spots:
                buttons[i]["text"] = "X"
                if (checkPlayerWin()):
                    entryFlag = False
                    buttons[i]["text"] = "O" # Dont let the player get that win
                    count += 1
                    break
                else:
                    buttons[i]["text"] = " " # Leave it as it was before

        # If both conditions dont exist, chose a random positon available
        if(entryFlag == True):
            entryFlag = False
            random_index = random.choice(available_spots)
            buttons[random_index]["text"] = "O"
            count += 1
                

# Button clicked function
def b_click(b):
    global count
    #checkWin()
    if (b["text"] == " ") and (count%2==0):
        b["text"] = "X"
        count += 1
        #checkWin()
        compMove()
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
buttons = [Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="silver", command=lambda x=i: b_click(buttons[x])) for i in range(9)]

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
