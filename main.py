import customtkinter as ctk
from minimax import *

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 


window = ctk.CTk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# set X , O on the buttons
def set_title(row, column):
    global currPlayer
    btn = Board[row][column]
    if btn.cget("text") == "":
        btn.configure(text=currPlayer)
        if currPlayer == "X":
            btn.configure(text_color="#E55050")
        else:
            btn.configure(text_color="#4A90E2")
        # Call Minimax Algorithm
        currPlayer = "O" if currPlayer == "X" else "X"
        label.configure(text=f"{currPlayer}'s Turn")


def restart():
    global currPlayer
    currPlayer = "X"
    for row in Board:
        for btn in row:
            btn.configure(text="")
    label.configure(text=f"{currPlayer}'s Turn")

# Main Frame
frame = ctk.CTkFrame(window)
frame.pack(padx=20, pady=20)

# Tic Tac Toe Label 
label = ctk.CTkLabel(frame, text=f"{currPlayer}'s Turn", font=ctk.CTkFont(size=20, weight="bold"))
label.grid(row=0, column=0, columnspan=3, pady=(0, 10))


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
            height=80,
            fg_color="#2e2e2e",
            hover_color="#333333",
            border_color="#444444",
            border_width=1,
            command=lambda r=row, c=column: set_title(r, c)
        )
        btn.grid(row=row, column=column, padx=8, pady=8)
        Board[row][column] = btn


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
