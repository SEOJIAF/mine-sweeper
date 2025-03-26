import tkinter as tk
from tkinter import ttk
import random 


def create_world(rows, cols, num_mines):
    world = [[0 for _ in range(cols)] for _ in range(rows)]
    mines = 0
    while mines < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if world[r][c] != "X":
            world[r][c] = "X"
            mines += 1
    return world

x = create_world(5, 5, 3)

flagged = []


def on_button_click(row, col, btn):
    b = check(row, col)
    if x[row][col] == "X":
        btn.config(text="Boom!", state="disabled")
        game_over_label = tk.Label(root, text="Game Over", font=("Helvetica", 24))
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        b = check(row, col)
        btn.config(text=str(b), state="disabled")

def on_right_click(event, row, col, btn):
    if (row, col) in flagged:
        style.configure("TButton", foreground="black")
        btn.config(style="TButton", text=f"{row},{col}")
        flagged.remove((row, col))
    else:
        style.configure("RedT.TButton", foreground="blue")
        btn.config(style="RedT.TButton", text="Flagged")
        flagged.append((row, col))
        flagged.sort()

    print(flagged)
    
    if flagged == x_positions:
        game_over_label = tk.Label(root, text="You win", font=("Helvetica", 24))
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")


root = tk.Tk()
root.title("Minesweeper")
root.geometry("400x400")

for i in range(5):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

def check(row, col):
    b = 0
    plus_row = row + 1
    min_row = row - 1
    plus_col = col + 1
    min_col = col - 1
    if 0 <= min_row < len(x) and 0 <= col < len(x[0]) and x[min_row][col] == "X":
        b += 1
        print("top")

    if 0 <= min_row < len(x) and 0 <= plus_col < len(x[0]) and x[min_row][plus_col] == "X":
        b += 1
        print("top right")

    if 0 <= row < len(x) and 0 <= plus_col < len(x[0]) and x[row][plus_col] == "X":
        b += 1
        print("right")

    if 0 <= plus_row < len(x) and 0 <= plus_col < len(x[0]) and x[plus_row][plus_col] == "X":
        b += 1
        print("down right")

    if 0 <= plus_row < len(x) and 0 <= col < len(x[0]) and x[plus_row][col] == "X":
        b += 1
        print("down")

    if 0 <= plus_row < len(x) and 0 <= min_col < len(x[0]) and x[plus_row][min_col] == "X":
        b += 1
        print("down left")

    if 0 <= row < len(x) and 0 <= min_col < len(x[0]) and x[row][min_col] == "X":
        b += 1
        print("left")

    if 0 <= min_row < len(x) and 0 <= min_col < len(x[0]) and x[min_row][min_col] == "X":
        b += 1
        print("top left")

    print("")
    print("")
    return b



x_positions = []

style = ttk.Style()
buttons = []

for i in range(len(x)):
    row_buttons = []
    for j in range(len(x[i])):
        btn = ttk.Button(root, text=f"{i},{j}")
        if x[i][j] == "X":
            style.configure("Red.TButton", foreground="red")
            btn.config(style="Red.TButton")
            x_positions.append((i, j))  

        btn.config(command=lambda r=i, c=j, b=btn: on_button_click(r, c, b)) 
        btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-3>", lambda e, r=i, c=j, b=btn: on_right_click(e, r, c, b))
        row_buttons.append(btn)

    buttons.append(row_buttons)

print("Positions of 'X':", x_positions)  

root.mainloop()
