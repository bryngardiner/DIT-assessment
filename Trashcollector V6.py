#260520 Trashcollector V1
#Bryn Gardiner

"""
************** Change Log ***************
V1.6 - Final product (with trash positions)
*****************************************
"""

#Variables
trashCollected = 0 #where trash picked up is stored

#map
gMap = [ #the map where you move
["X","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",],
["O","O","O","O","O","O","O",]
]

#position of the player
playerPos = (0,7)
trash1 = [1,7]
trash2 = [3,4]
trash3 = [2,5]
 

#define functions

def setPos(pos,letter):
   global gMap
   gMap[7-pos[1]][pos[0]] = letter
   
 # Check if a position is on the board.
def isPosValid(pos):
   if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
      return False
   return True

# Returns FALSE if the player tried to move off the board
def movePlayer(moveOffset):
   global playerPos
   # Move pos
   newPos = (playerPos[0]+moveOffset[0],playerPos[1]+moveOffset[1])
   # Check if moved off the board
   if not isPosValid(newPos):
      return False
   # Update board
   setPos(playerPos,"O")
   setPos(newPos,"X")
   playerPos = newPos
   return True
   
def move(): #the function that moves the player on the map
   displayMap()
   print("wasd to move")
   userInput = input(">>>  ")
   
   if userInput.lower() == "w":
      moveOffset = (0,1)   
   elif userInput.lower() == "a":
      moveOffset = (-1,0)  
   elif userInput.lower() == "s":
      moveOffset = (0,-1)
   elif userInput.lower() == "d":
      moveOffset = (1,0)
   else:
      print("You no enter right ting!")
      return
   # If the player tried to move to an invalid location
   if not movePlayer(moveOffset):
      print("You can't move there")
      return
   
def displayMap(): #displays the map to the player
   print("\n".join([" ".join(line) for line in gMap]))
   

def displayStats(): #shows how much trash the player currently has 
   print("""
********* Stats ************
Trash: %d

***********************************
    """%trashCollected) #prints trash number as a digit


#intro text

print("Pick up all the trash so the earth is saved") #go ahead and pick up the trash already 

#user interface

while trashCollected <3: #this will keep looking for trash until you get 3 trash
   move()
   if playerPos == (1,7): #if the player is in this location it will pick of trash
      print("You got trash")
      trashCollected += 1
   if playerPos == (3,4):
      print("You got trash")
      trashCollected += 1
   if playerPos == (2,5):
      print("You got trash")
      trashCollected += 1  
   displayStats()

print("You got all the trash and earth is saved") #congratulations, you win
