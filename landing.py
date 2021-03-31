#landing page for admins after logged in

import tkinter as tk
import player
import FindPlayer
import stats
import addPlayer
import changePlayerInfo

class HomeWin(FindPlayer.Win1):
 
    def show_widgets(self,x):
        self.master.title('Home')
        self.frame = tk.Frame(self.master)
        self.players_button = tk.Button(
            self.frame, text=f"Find players",
            command=self.showPlayersWin)
        self.players_button.pack()
        self.frame.pack() 

        self.statistics_button = tk.Button(
            self.frame, text=f"View Statistics",
            command=self.showStatsWin)
        self.statistics_button.pack()

        self.newPlayer_button = tk.Button(
            self.frame, text=f"Add a Player",
            command=self.showAddPlayerWin)
        self.newPlayer_button.pack()


#Opens players window
    def showPlayersWin(self):
      root2= tk.Tk()
      FindPlayer.Win1(root2, 'home')
      root2.mainloop()
    
#Opens statistics window
    def showStatsWin(self):
      root3 = tk.Tk()
      stats.Win1(root3,'stats')
      root3.mainloop()

#Opens new player window
    def showAddPlayerWin(self):
      root4 = tk.Tk()
      addPlayer.Win1(root3)
      root4.mainloop()
    
#Opens change player info window
    def showChangePlayerInfo(self):
      root5 = tk.Tk()
      changePlayerInfo.Win1(root5)
      root5.mainloop()

  