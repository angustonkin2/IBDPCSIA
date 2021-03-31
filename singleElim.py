from replit import db
from binarytree import tree, bst, heap, Node, build
import math
import random
import player

def singleElim():
  #User choses the size of the tournament
  tournSize = 8
  
  #Fills the array with null objects depending on tournment size
  values = []
  counter = 0
  while counter < tournSize - 1:
    values.append(0)
    counter = counter + 1

  #Creates array and fills it with the ranking ID of players in the tournament
  tournPlayers = []
  n = 1
  while n < tournSize + 1:
    tournPlayers.append(n)
    n = n + 1
  

  tournPlayers = choseBracket(tournSize, tournPlayers)
  
  #Appends ordered players array onto the tree values array
  for i in range(tournSize):
    values.append(tournPlayers[i])

  #Checking that tournament is the correct size and printing it
  if tournSize == 8 or 16 or 32 or 64 or 128:
      print('You are playing a',tournSize,'player tournament')  
  else:
    print('Wrong size')


  beginRounds(tournSize, tournPlayers, values)
  
  

def beginRounds(tournSize,tournPlayers, values):
  currentRound = 0
  playersLeft = len(tournPlayers)
  roundsLeft = 1

  while roundsLeft > 0:
    roundsLeft = int(math.log2(len(tournPlayers)))
    if roundsLeft == 1:
      currentRound = 'Final'
    elif roundsLeft == 2:
      currentRound = 'SemiFinal'
    elif roundsLeft == 3:
      currentRound = 'QuarterFinal'

    #Building the initial binary tree for the tournament from the given array of players and 0 spots
    #Printing the binarytree for current round
    tree = build(values)
    print(tree)
    if currentRound == 'Final':
      print(currentRound,'Round match:')
    else:
      print(currentRound,'Round matches:')
    

    k = 0
    j = 0
    matches = []
    while k < len(tournPlayers)/2:
      matches.append([tournPlayers[j], tournPlayers[j+1]])
      k = k + 1
      j = j + 2
    
    b = 0
    while len(tournPlayers) > b:
      first = b
      second = b + 1
      print((player.players[first])['name'],'vs', (player.players[second])['name'])
      b = b + 2
      
    loserArray = []
    for i in range(len(matches)):  
      loser = random.choice(matches[i])
      loserArray.append(loser)
      matches[i].remove(loser)
      winner = (matches[i])[0]
      print(winner)
    x = len(loserArray)
    for i in range(x):
      tournPlayers.remove(loserArray[i])
      values.remove(loserArray[i])
    numZeros = len(tournPlayers)
    for i in range(numZeros):
      del(values[0])
    if roundsLeft == 1:
      roundsLeft = 0
      tournwinner = tournPlayers[-1]
      print("The winner is",(player.players[tournwinner-1])['name'])
    

   
#Rearranges the binary tree according to which type of bracket the user wants
def choseBracket(tournSize, tournPlayers):
  bracketType = 'random'
  #Arranging array for random brackets
  if bracketType == 'random':
    tournPlayers = random.sample(tournPlayers, tournSize)
    return(tournPlayers)
  #Arranging array for seeded brackets
  elif bracketType == 'seeded':
    tempList = []

    while len(tournPlayers) > 0:
      tempList.append(tournPlayers[0])
      tournPlayers.remove(tournPlayers[0])
      tempList.append(tournPlayers[-1])
      tournPlayers.remove(tournPlayers[-1])
    return tempList

      


#Prints the bottom numbers in order from a given binary tree
def postOrderTrav(my_tree):
  if my_tree.left != None:
    postOrderTrav(my_tree.left)
  if my_tree.right != None:
    postOrderTrav(my_tree.right)
  if my_tree.right == None and my_tree.left == None:
    print(my_tree.value)
  

