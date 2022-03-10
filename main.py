import singleplayer
from host import host, setupHosting

def multiUser():
  yNo = input("Would you like to host? ")
  if 'y' or 'Y' in yNo:
    setupHosting()
    host(host.route, host.userPort)

print("Welcome to cave explorer, a MUSH game.")
user = input("Would you like to play Multiplayer?")
if "y" in user:
    multiUser()