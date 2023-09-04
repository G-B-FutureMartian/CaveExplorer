from flask import Flask
from time import sleep
app = Flask(__name__)

def setupHosting():
  print("Now it's time to setup your server.")
  sleep(1)
  print("What port would you like to use?")
  userPort = input()
  sleep(.25)
  print("Thanks!")
  sleep(0.5)
  print("That's half over the work done already. Easy, right?")
  sleep(0.5)
  print("For organization, what type or user are you?")
  sleep(.5)
  print("D for dev/playtester, N for normal Enduser-")
  sleep(.25)
  print("- if you don't know, type N.")
  rawRoute = input()
  if 'n' or 'N' in rawRoute:
    global route
    route = "/"
  elif 'a' or 'A' in rawRoute:
    route = "/admin"
  return userPort, route

def host(route, userPort):
  @app.route(route)
  def index():
    return("Hello, World")
  sleep(3)
  app.run(debug=False, host="0.0.0.0", port=userPort)

if __name__ == "__main__":
  print("You will begin hosting an empty room.")
  print("You will be using the Flask framework for a local server.")
  if "y" in input("Ok? y/n"):
    print("Great!")
    setupHosting()
    host()
