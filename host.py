from flask import Flask
from time import sleep
app = Flask(__name__)

def host(route, userPort):
  @app.route(route)
  def index():
    return("Hello, World")
  sleep(3)
  app.run(debug=False, host="0.0.0.0", port=userPort)

if __name__ == "__main__":
  print("You will now begin hosting an empty room.")
  print("You will be using the Flask framework for a local server.")
  if input("Ok? ") == "Yes" or "yes":
    print("Good.")