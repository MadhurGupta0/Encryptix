import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import subprocess

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("675x450")
root.configure(background="#000000")

# Load rock, paper, and scissors images
rock_img = Image.open("rock.jpg")  # Replace with your own image file
paper_img = Image.open("paper.jpg")  # Replace with your own image file
scissors_img = Image.open("scissors.jpg")  # Replace with your own image file

# Resize images to fit the buttons
rock_img = rock_img.resize((98, 100))
paper_img = paper_img.resize((98, 100))
scissors_img = scissors_img.resize((98,100))

# Convert images to PhotoImage format
rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)


user_score = 0
computer_score = 0
d=[]
res="tie"
inde=0
# Function to determine the winner
def play_game(user_choice):
    global user_score, computer_score,res
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if (computer_choice=="Rock"):
        comp_choice_label=tk.Label(root,image=rock_photo)
    elif (computer_choice=="Paper"):
        comp_choice_label=tk.Label(root,image=paper_photo)
    elif (computer_choice=="Scissors"):
        comp_choice_label=tk.Label(root,image=scissors_photo)

    if (user_choice=="Rock"):
        user_choice_label=tk.Label(root,image=rock_photo)
    elif (user_choice=="Paper"):
        user_choice_label=tk.Label(root,image=paper_photo)
    elif (user_choice=="Scissors"):
        user_choice_label=tk.Label(root,image=scissors_photo)

    user_choice_label.grid(row=2,column=2)
    comp_choice_label.grid(row=2,column=4)
               
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
        res="Tie"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You win!")
        user_score += 1
        res="User"
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1
        res="Computer"


    d.append((user_choice,computer_choice,res))
    if len(d)%8==0:
        show_winner_popup()


    # Update score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    # Display computer's choice

def show_winner_popup():
    global popup,inde
    winner = "You" if user_score > computer_score else "Computer"
    popup = tk.Toplevel(root)
    popup.title("Game Over")
    popup_label = tk.Label(popup, text=f"{winner} wins the game!", font=("Helvetica", 14))
    popup_label.pack()
    
    my_game = ttk.Treeview(popup, columns=('User', 'Computer', 'Winner'))
    my_game.heading("#0", text="Round Number", anchor="center")
    my_game.heading("User", text="User", anchor="center")
    my_game.heading("Computer", text="Computer", anchor="center")
    my_game.heading("Winner", text="Winner", anchor="center")

    
    for i, (name, score, rank) in enumerate(d[inde:]):
        print(inde,"index")
        my_game.insert(parent='', index='end', iid=i, text=str(i + 1), values=(name, score, rank))

    my_game.pack()
    
    
    new_game_button = tk.Button(popup, text="New Game", command=start_new_game)
    new_game_button.pack()
    inde+=8


# Function to start a new game
def start_new_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose Rock, Paper, or Scissors!")
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    tk.Label(root,width=14,height=10,bg= "#000000").grid(row=2,column=4)
    tk.Label(root,width=14,height=10,bg= "#000000" ).grid(row=2,column=2)
    popup.destroy()
    

# Create buttons with images
rock_button = tk.Button(root, image=rock_photo, command=lambda: play_game("Rock"))
paper_button = tk.Button(root, image=paper_photo, command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, image=scissors_photo, command=lambda: play_game("Scissors"))
comp_rock_lable=tk.Label(root,image=rock_photo)
comp_scissors_lable=tk.Label(root,image=scissors_photo)
comp_paper_lable=tk.Label(root,image=paper_photo)
# Arrange buttons in the window

rock_button.grid(row=1, column=1)
paper_button.grid(row=2, column=1)
scissors_button.grid(row=3, column=1)

comp_rock_lable.grid(row=1, column=5)
comp_paper_lable.grid(row=2, column=5)
comp_scissors_lable.grid(row=3, column=5)
# Create a label to display the result
result_label = tk.Label(root,width=25,height=2,bg="#000000",fg="white",text="Choose Rock, Paper, or Scissors!")
result_label.grid(row=3, column=3)

# Create labels for scores
user_score_label = tk.Label(root,width=20,height=2,bg="#000000",fg="white", text="Your Score: 0")
computer_score_label = tk.Label(root,width=20,height=2,bg="#000000",fg="white", text="Computer Score: 0")
user_score_label.grid(row=1, column=3)
computer_score_label.grid(row=2, column=3)
comp_choice_label=tk.Label(root,width=14,height=10,bg="#000000" ).grid(row=2,column=4)
user_choice_label=tk.Label(root,width=14,height=10, bg="#000000" ).grid(row=2,column=2)
# Label to display computer's choice

tk.Label(root,width=12,height=2,bg="#000000",text="User",fg="white",font=("Arial", 14)).grid(row=0,column=1)
tk.Label(root,width=12,height=2,bg="#000000",text="Computer",fg="white",font=("Arial", 14)).grid(row=0,column=5)

# Start the GUI event loop

button = ttk.Button(root, text="Back to Start Page", command=lambda:(root.destroy(),subprocess.run(['python', 'rps.py'])))
button.grid(row=5, column=3, padx=10, pady=10)
root.mainloop()
 

