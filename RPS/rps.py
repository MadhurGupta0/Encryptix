import tkinter as tk 
import subprocess


LARGEFONT = ("Verdana", 35)
def main_menu():
    
        self=tk.Tk()
        self.title("Rock-Paper-Scissors Game")
        self.config(background="#000000")
        tk.Label(self, width=14,height=1,text="",bg="#000000", font=LARGEFONT).pack()
        label = tk.Label(self, text="Start Game",bg="#000000",fg="white",font=LARGEFONT)
        label.pack()
        
        tk.Label(self, width=14,height=1,text="", bg="#000000",font=LARGEFONT).pack()

        button1 = tk.Button(self, text="Single Player", command=lambda: (self.destroy(),show_frame_page1("Page1")))
        button1.pack()
        tk.Label(self, width=14,height=1,text="",bg="#000000").pack()

        button2 = tk.Button(self, text="Multi Player", command=lambda: (self.destroy(),show_frame("Page2")))
        button2.pack()
        tk.Label(self, width=14,height=1,text="",bg="#000000").pack()
        self.mainloop()
        
        
def show_frame_page1(frame):
    subprocess.run(['python', 'SinglePlayer.py'])
def show_frame(frame):
    
    subprocess.Popen(['python', 'server.py'])
    subprocess.Popen(['python', 'client.py'])
    subprocess.Popen(['python', 'client.py']).wait()
    

main_menu()