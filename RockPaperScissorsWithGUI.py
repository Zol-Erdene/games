import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("250x300+10+20")
window.minsize(250, 300)
window.maxsize(250, 300)

def resolve_winner(human, cpu):
    if human == "ROCK":
        if cpu == "ROCK":
            output_text.insert(tk.END, "Draw!")
            score[2] += 1
        elif cpu == "PAPER":
            output_text.insert(tk.END, "You lose.") 
            score[1] += 1
        else:
            output_text.insert(tk.END, "You win.") 
            score[0] += 1
    elif human == "PAPER":
        if cpu == "PAPER":
            output_text.insert(tk.END, "Draw!")
            score[2] += 1
        elif cpu == "SCISSORS":
            output_text.insert(tk.END, "You lose.") 
            score[1] += 1
        else:
            output_text.insert(tk.END, "You win.") 
            score[0] += 1
    else:
        if cpu == "SCISSORS":
            output_text.insert(tk.END, "Draw!")
            score[2] += 1
        elif cpu == "ROCK":
            output_text.insert(tk.END, "You lose.") 
            score[1] += 1
        else:
            output_text.insert(tk.END, "You win.") 
            score[0] += 1
    output_text.insert(tk.END, "\n") 
    output_text.see("end")
    update_score()

def update_score():
    score_str = f"Player: {score[0]}  CPU: {score[1]}  Draws: {score[2]}"
    score_board.config(text=score_str)

def CPU_turn():
    options = ["ROCK", "PAPER", "SCISSORS"]
    cpu_selection = random.choice(options)
    output_text.insert(tk.END, f"CPU played {cpu_selection}.\n")
    return cpu_selection

def on_rock_click():
    output_text.insert(tk.END, "You played ROCK.\n")
    cpu_selection = CPU_turn()
    
    resolve_winner("ROCK", cpu_selection)

def on_paper_click():
    output_text.insert(tk.END, "You played PAPER.\n")
    cpu_selection = CPU_turn()
    resolve_winner("PAPER", cpu_selection)

def on_scissors_click():
    output_text.insert(tk.END, "You played SCISSORS.\n")
    cpu_selection = CPU_turn()
    resolve_winner("SCISSORS", cpu_selection)


lbl = tk.Label(window, text="Play rock-paper-scissors!", font=(20))
lbl.place(x=30, y=10)

intro_text = tk.Label(window, text="Computer randomly plays one the options.")
intro_text.place(x=10, y= 40)

score = [0, 0, 0]
score_board = tk.Label(window, text=f"Player: {score[0]}  CPU: {score[1]}  Draws: {score[2]}")
score_board.place(x=50, y=60)

rock_btn = tk.Button(window, text="Rock", fg="blue", width=5, command=on_rock_click)
rock_btn.place(x=45, y=90)

paper_btn = tk.Button(window, text="Paper", fg="blue", width=5, command=on_paper_click)
paper_btn.place(x=95, y=90)

scissors_btn = tk.Button(window, text="Scissors", fg="blue", width=5, command=on_scissors_click)
scissors_btn.place(x=145, y=90)

output_text = tk.Text(window, height=10, width=25)
output_text.place(x=10, y=120)

output_text.insert(tk.END, "Please make a selection.\n")

window.mainloop()