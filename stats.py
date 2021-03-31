import tkinter as tk
import player 


class Win1:
  def __init__(self, master, info):
      self.master = master
#Defines size of windows
      self.master.geometry("400x300")
#Adds 
      self.show_widgets(info)
      self.name = info
      
  def show_widgets(self, x):
#Creating window frame
      self.frame = tk.Frame(self.master)
#Heading of window
      self.master.title("Statistics")
      x = list(player.p1.keys())
      c=0
      r=0
      #self.create_button('hello',Win2,'i',c,r)
      for i in x:
        self.create_button(i,Win2,i,c,r)
        if c != 4:
          c = c+2
        else:
          c = 0
          r = r+2
  def processStats(self,info):
    for i in player.players:
      print(i[info])
  #Creating buttons for every player profile
  #Function to create a custom button
  def create_button(self, text, _class, info,c,r):
    #  "Button that creates a new window"
    #tk.Button(self.frame, text=text,command=lambda: self.new_window(_class, info)).grid(row=r,column=c)
    button1=tk.Button(self.master, text=text,command=lambda:self.new_window(_class,info))
    button1.grid(row=r,column=c)


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
        self.master.title(info)
        self.frame = tk.Frame(self.master, bg="red")
        self.quit_button = tk.Button(
            self.frame, text=f"Go back",
            command=self.close_window)
        self.quit_button.pack()

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