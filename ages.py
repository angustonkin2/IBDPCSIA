import player

def bubblesort(numbers):
    sorted = False
       
    while not sorted:
        sorted = True
        for i in range(len(numbers) -1):
            if numbers[i]['age'] > numbers[i+1]['age']:
                sorted = False
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                
        if sorted:
            return numbers

def getOldest():
  list = []
  for i in player.players:
    list.append(i)
  bubblesort(list)
  print(list[-1]['name'])

def getYoungest():
  list = []
  for i in player.players:
    list.append(i)
  bubblesort(list)
  print(list[0]['name'])
