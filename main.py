import singleplayer
from host import host, setupHosting
from join import joinGameStream

def multiUser():
  yNo = input("Would you like to host? ")
  if 'y' or 'Y' in yNo:
    userPort,route = setupHosting()
    host(route, userPort)
  elif 'n' in yNo:
    port = input("What port do you need?")
    joinGameStream(port.int())
    print("Nothing here right now.")

print("Welcome to cave explorer, a MUSH game.")
users = input("Would you like to play Multiplayer?")
if "y" in users:
    multiUser() 
else:
    pass
