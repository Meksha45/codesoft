import tkinter as tk
from tkinter import messagebox
import random

# Global scores
user_score = 0
computer_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Game Logic
def determine_winner(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n{result}")
    score_label.config(text=f"Score → You: {user_score}  Computer: {computer_score}")

# Play Again (Reset UI)
def play_again():
    result_label.config(text="Make your choice!")
    # Optionally reset scores:
    # global user_score, computer_score
    # user_score = computer_score = 0
    # score_label.config(text="Score → You: 0  Computer: 0")

# Exit the Game
def exit_game():
    root.destroy()

# Main GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

# Labels
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: determine_winner(c)).pack(side=tk.LEFT, padx=10)

# Play Again and Exit Buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

tk.Button(bottom_frame, text="Play Again", font=("Arial", 12), command=play_again).pack(side=tk.LEFT, padx=20)
tk.Button(bottom_frame, text="Exit", font=("Arial", 12), command=exit_game).pack(side=tk.RIGHT, padx=20)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

# Global scores
user_score = 0
computer_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Game Logic
def determine_winner(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n{result}")
    score_label.config(text=f"Score → You: {user_score}  Computer: {computer_score}")

# Play Again (Reset UI)
def play_again():
    result_label.config(text="Make your choice!")
    # Optionally reset scores:
    # global user_score, computer_score
    # user_score = computer_score = 0
    # score_label.config(text="Score → You: 0  Computer: 0")

# Exit the Game
def exit_game():
    root.destroy()

# Main GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

# Labels
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: determine_winner(c)).pack(side=tk.LEFT, padx=10)

# Play Again and Exit Buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

tk.Button(bottom_frame, text="Play Again", font=("Arial", 12), command=play_again).pack(side=tk.LEFT, padx=20)
tk.Button(bottom_frame, text="Exit", font=("Arial", 12), command=exit_game).pack(side=tk.RIGHT, padx=20)

root.mainloop()
