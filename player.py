

# Defining keys that each dictionary will have
Angus = {
  'name':'Angus',
  'age':'17',
  'height':175+'cm',
  'plays':'right handed'
  
}

Bob = {
  'name':'Bob',
  'age':'42',
  'height':'201cm',
  'plays':'left'
  
}
# List storing all players
players = [Angus, Bob]

def getProfile(ent):
  name = ent.get()
  i = 0
  found = False
  while found == False and i < len(players):
    player = players[i]
    if player['name'] == name:
      found = True
      print(player)
    i = i+1
  if found == False:
    print('No player')
    
    
  
  
  
  
  
def newPlayer(name,age,height,plays):
  name = ent.get()
  name = 
  
  }






 
  
 
  


