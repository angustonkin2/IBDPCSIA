import tkinter as tk
#import player
import names 

#Finding a random full name
#print(names.get_full_name(gender='male'))

root= tk.Tk() # Establishes a root

#Initialises tkinter
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised') 
canvas1.pack()

# Makes label
label1 = tk.Label(root, text='Search a player profile')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1) # coordinates of canvas

label2 = tk.Label(root, text='Enter player name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) # Creating a field
canvas1.create_window(200, 140, window=entry1)


  
def test():
  print('testing')
#button1 = tk.Button(text='Search a player profile', command= test, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button1 = tk.Button(text='Search a player profile', command= lambda:player.getProfile(entry1), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()



