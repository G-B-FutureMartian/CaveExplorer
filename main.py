import sys
from singleplayer import Hello

print("Welcome to cave explorer, a MUSH exploration game.")
user = input("Would you like to play Multiplayer?")
if user == "Yes" or "yes" or "y":
    Hello()