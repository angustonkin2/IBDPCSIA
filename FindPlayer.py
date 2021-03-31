import tkinter as tk
import player
from PIL import Image, ImageTk



class Win1:
    def __init__(self, master, info):
        self.master = master
        self.master.geometry("400x300")
        self.show_widgets(info)
        self.name = info
        
#
    def show_widgets(self, x):
#Creating window frame
        self.frame = tk.Frame(self.master)
        self.master.title("Tennis Players")
        self.frame.pack()
#Creating buttons for every player profile
        for i in range(len(player.players)):
          myPlayer = player.players[i]
          self.create_button(myPlayer['name'],Win2, myPlayer )
        
        
#Function to create a custom button
    def create_button(self, text, _class, info):
      #  "Button that creates a new window"
        tk.Button(
            self.frame, text=text,
            command=lambda: self.new_window(_class, info)).pack()


    def new_window(self, _class, info):
            global win2, win3
 
            try:
                if _class == Win2:
                  if win2.state() == "normal" and win2.name ==info['name']:
                      win2.focus()
            except:  
                win2 = tk.Toplevel(self.master)
                _class(win2, info)
 
            try:
                if _class == Win3:
                    if win3.state() == "normal":
                        win3.focus()
            except:  
                win3 = tk.Toplevel(self.master)
                _class(win3, info)
 
    def close_window(self):
        self.master.destroy()
 
class Win2(Win1):
 
    def show_widgets(self,x):
        self.master.title(x['name'])
        self.frame = tk.Frame(self.master, bg="red")
        self.quit_button = tk.Button(
            self.frame, text=f"Go back",
            command=self.close_window)
        self.quit_button.pack()
#Labels for each player statistic
        ageLabel = tk.Label(self.master, text='age: ' + str(x['age'])).place(x = 40, y = 40)
        sexLabel = tk.Label(self.master, text='sex: ' + x['sex']).place(x =40 , y = 60)
        countryLabel = tk.Label(self.master, text='country: ' + x['country']).place(x =40 , y = 80)
        heightLabel = tk.Label(self.master, text='height: ' + x['height']).place(x =40 , y = 100)
        playsLabel = tk.Label(self.master, text='plays: ' + x['plays']).place(x =40 , y = 120)
        winsLabel = tk.Label(self.master, text='wins: ' + str(x['wins'])).place(x =40 , y = 140)
        lossesLabel = tk.Label(self.master, text='losses: ' + x['losses']).place(x =40 , y = 160)
        rankingLabel = tk.Label(self.master, text='ranking: ' + x['ranking']).place(x =40 , y = 180)
        tournamentwinsLabel = tk.Label(self.master, text='tournament wins: ' + x['tournament wins']).place(x =40 , y = 200)
        matchesLabel = tk.Label(self.master, text='tournament wins: ' + x['tournament wins']).place(x =40 , y = 200)
        matchesplayedLabel = tk.Label(self.master, text='matches played: ' + x['matches played']).place(x =40 , y = 220)


        #displayImage.displayImage(self.master)
      
        
        
        
        self.frame.pack()
 
 

class Win3(Win2):
 
    def show_widgets(self):
        self.master.title("Window 3")
        self.frame = tk.Frame(self.master, bg="green")
        self.quit_button = tk.Button(
            self.frame, text="Quit this window n. 3",
            command=self.close_window)
        self.label = tk.Label(
            self.frame, text="THIS IS ONLY IN THE THIRD WINDOW")
        self.label.pack()
        self.frame.pack()



 
 
  