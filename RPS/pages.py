import tkinter as tk
from network import Network

width = 700
height = 700

class Button:
    def __init__(self, text, x, y, color, command=None):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100
        self.command = command

    def create(self, win):
        button = tk.Button(win, text=self.text, bg=self.color, fg='white', font=("comicsans", 20),
                           width=self.width//10, height=self.height//30, command=self.command)
        button.place(x=self.x, y=self.y)
        return button

def redrawWindow(win, game, player, btns):
    for widget in win.winfo_children():
        widget.destroy()
    
    if not game.connected():
        label = tk.Label(win, text="Waiting for Player...", font=("comicsans", 30), fg="red")
        label.place(x=width/2 - label.winfo_reqwidth()/2, y=height/2 - label.winfo_reqheight()/2)
    else:
        label_your_move = tk.Label(win, text="Your Move", font=("comicsans", 25), fg="cyan")
        label_your_move.place(x=80, y=200)

        label_opponents = tk.Label(win, text="Opponents", font=("comicsans", 25), fg="cyan")
        label_opponents.place(x=380, y=200)

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.bothWent():
            label_move1 = tk.Label(win, text=move1, font=("comicsans", 20), fg="black")
            label_move2 = tk.Label(win, text=move2, font=("comicsans", 20), fg="black")
        else:
            if game.p1Went and player == 0:
                label_move1 = tk.Label(win, text=move1, font=("comicsans", 20), fg="black")
            elif game.p1Went:
                label_move1 = tk.Label(win, text="Locked In", font=("comicsans", 20), fg="black")
            else:
                label_move1 = tk.Label(win, text="Waiting...", font=("comicsans", 20), fg="black")

            if game.p2Went and player == 1:
                label_move2 = tk.Label(win, text=move2, font=("comicsans", 20), fg="black")
            elif game.p2Went:
                label_move2 = tk.Label(win, text="Locked In", font=("comicsans", 20), fg="black")
            else:
                label_move2 = tk.Label(win, text="Waiting...", font=("comicsans", 20), fg="black")

        if player == 1:
            label_move2.place(x=100, y=350)
            label_move1.place(x=400, y=350)
        else:
            label_move1.place(x=100, y=350)
            label_move2.place(x=400, y=350)

        for btn in btns:
            btn.create(win)

def handle_button_click(btn, game, player, n, win, btns):
    if player == 0 and not game.p1Went:
        n.send(btn.text)
    elif player == 1 and not game.p2Went:
        n.send(btn.text)
    
    # Force a redraw after the button is pressed
    redrawWindow(win, game, player, btns)

def game_loop(n,player,btns):
    last_game_state = None
    
    def loop():
        nonlocal last_game_state
        try:
            global game
            game = n.send("get")
        except:
            print("Couldn't get game")
            win.quit()
            return

        # Only redraw if the game state has changed
        if game != last_game_state:
            redrawWindow(win, game, player, btns)
            last_game_state = game

        if game.bothWent():
            win.after(500, lambda: n.send("reset"))

            label_result = tk.Label(win, text="You Won!" if (game.winner() == 1 and player == 1) or 
                                               (game.winner() == 0 and player == 0) else 
                                               "Tie Game!" if game.winner() == -1 else 
                                               "You Lost...", font=("comicsans", 30), fg="red")
            label_result.place(x=width/2 - label_result.winfo_reqwidth()/2, y=height/2 - label_result.winfo_reqheight()/2)
            win.after(2000, loop)
            return

        win.after(1000, loop)

    loop()

def main():
    global win
    win = tk.Tk()
    win.title("Client")
    win.geometry(f"{width}x{height}")

    n = Network()
    player = int(n.getP())
    print("You are player", player)

    btns = [
        Button("Rock", 50, 500, "black", command=lambda: handle_button_click(btns[0], game, player, n, win, btns)),
        Button("Scissors", 250, 500, "red", command=lambda: handle_button_click(btns[1], game, player, n, win, btns)),
        Button("Paper", 450, 500, "green", command=lambda: handle_button_click(btns[2], game, player, n, win, btns))
    ]

    game_loop(n,player,btns)
    win.mainloop()

def menu_screen():
    win = tk.Tk()
    win.title("Client")
    win.geometry(f"{width}x{height}")

    label = tk.Label(win, text="Click to Play!", font=("comicsans", 40), fg="red")
    label.pack(expand=True)

    def start_game(event):
        win.destroy()
        main()

    win.bind("<Button-1>", start_game)
    win.mainloop()

menu_screen()
