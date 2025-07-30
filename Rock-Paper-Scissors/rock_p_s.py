import tkinter as tk
import random

def play(choice):
    computer = random.choice(["rock", "paper", "scissors"])
    
    if choice == computer:
        result = "Draw!"
    elif (choice == "rock" and computer == "scissors") or \
         (choice == "paper" and computer == "rock") or \
         (choice == "scissors" and computer == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer}\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

title = tk.Label(root, text="Rock Paper Scissors ?", font=("Arial", 20))
title.pack(pady=10)

rock_button = tk.Button(root, text="🪨 Rock", width=15, command=lambda: play("rock"))
paper_button = tk.Button(root, text="📄 Paper", width=15, command=lambda: play("paper"))
scissors_button = tk.Button(root, text="✂️ Scissors", width=15, command=lambda: play("scissors"))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()