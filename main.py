import singleplayer
from host import host, setupHosting
from join import joinGameStream

def multiUser():
  yNo = input("Would you like to host? ")
  if 'y' in yNo:
    userPort,route = setupHosting()
    host(route, userPort)
  elif 'n' in yNo:
    port = input("What port do you need?")
    joinGameStream(int(port))
    #print("Nothing here right now.")

print("Welcome to cave explorer, a MUSH game.")
users = input("Would you like to play Multiplayer?")
if 'y' in users:
    multiUser() 
else:
    print('Perfecto')
