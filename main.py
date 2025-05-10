import customtkinter as ctk
from minimax import *
import time
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 


window = ctk.CTk()
window.title("Tic Tac Toe")
window.resizable(False, False)

Board = [['','',''],
         ['','',''],
         ['','','']]
board_buttons = [[None, None, None], [None, None, None], [None, None, None]]
game_over = False

# Main Frame
frame = ctk.CTkFrame(window)
frame.pack(padx=20, pady=20)

    
def change_Title():
    winner = checkWinner(Board)
    # winner = 'X'
    if (winner == None):
        title = f"{currPlayer}'s Turn"
    elif winner == "Tie":
        title = "Tie"
    else :
        title = f"{winner} Wins"
    return title


def set_title(row, column):
    global game_over
    if game_over == True:
        return
    global currPlayer
    btn = board_buttons[row][column]
    if btn.cget("text") == "":
        btn.configure(text=currPlayer)
        Board[row][column] = currPlayer
        btn.configure(text_color="#E55050" if currPlayer == "X" else "#4A90E2")

        winner = checkWinner(Board)
        if winner:
            label.configure(text=change_Title(),text_color="#F3C623")
            for row in board_buttons:
                for btn in row:
                    btn.configure(state="disabled")
            game_over = True 
        else:
            currPlayer = "O" if currPlayer == "X" else "X"
            label.configure(text=change_Title())
        if currPlayer == 'O':
            window.after(800, AI)  # 2000 ميلي ثانية = 2 ثانية

def AI():
    # time.sleep(2)
    row , col = AI_Move(Board)
    set_title(row,col)
    
def restart():
    global game_over
    game_over = False
    global currPlayer, Board
    currPlayer = "X"
    Board = [['','',''],
             ['','',''],
             ['','','']]
    for row in board_buttons:
        for btn in row:
            btn.configure(text="", state="normal")
    label.configure(text=f"{currPlayer}'s Turn")

# # Tic Tac Toe Label 
label = ctk.CTkLabel(frame, text=f"{change_Title()}", font=ctk.CTkFont(size=20, weight="bold"))
label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
 #----------------------------------------------------------------------------------------------
# Buttons Border
buttons_frame = ctk.CTkFrame(frame, fg_color="#222222", border_color="#444444", border_width=2)
buttons_frame.grid(row=1, column=0, columnspan=3, padx=8, pady=8)

# Create Buttons
for row in range(3):
    for column in range(3):
        btn = ctk.CTkButton(
            buttons_frame,
            text="",
            font=("Consolas",50,"bold"),
            width=120,
            height=100,
            fg_color="#2e2e2e",
            hover_color="#333333",
            border_color="#444444",
            border_width=1,
            command=lambda r=row, c=column: set_title(r, c)
        )
        btn.grid(row=row, column=column, padx=8, pady=8)
        board_buttons[row][column] = btn


# Restart Button
restart_btn = ctk.CTkButton(frame, text="Restart", fg_color="blue", hover_color="darkblue", command=restart)
restart_btn.grid(row=4, column=0, columnspan=3, pady=(10, 0), sticky="we")

# Center window in the Screen
window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
