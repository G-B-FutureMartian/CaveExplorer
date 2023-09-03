import singleplayer
from host import hosting, setupHosting
import join

def multiUser():
  yNo = input("Would you like to host? ")
  if 'y' or 'Y' in yNo:
    setupHosting()
    hosting(setupHosting.route, setupHosting().userPort)
  elif 'n' or 'N' in yNo:
    print("Nothing here right now.")

print("Welcome to cave explorer, a MUSH game.")
user = input("Would you like to play Multiplayer?")
if "y" in user:
    multiUser() 
