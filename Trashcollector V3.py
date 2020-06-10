#260520 Trashcollector V1
#Bryn Gardiner

"""
************** Change Log ***************
V1.3 - The map 
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

def setPos(pos,letter):
   global gMap
   gMap[7-pos[1]][pos[0]] = letter
   
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

print("You got all the trash and earth is saved") #congratulations, you win
