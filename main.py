import singleplayer
from host import host, setupHosting
import join

def multiUser():


  yNo = input("Would you like to host? ")
  if 'y' or 'Y' in yNo:
    userPort,route = setupHosting()
    host(route, userPort)
  elif 'n' in yNo:

  
    print("Nothing here right now.")

print("Welcome to cave explorer, a MUSH game.")
users = input("Would you like to play Multiplayer?")
if "y" in users:
    multiUser() 
else:
    pass
