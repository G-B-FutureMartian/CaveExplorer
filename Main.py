from random import choice, randint

print("Welcome to cave explorer, a MUSH exploration game."
clientType = input("Client or host?")
if clientType == "Host" or "host":
   from flask import Flask, render_template
   serverPort = input("What initial server port?")
   
   app = Flask(__name__)
   
   @app.route("/")
   def index():
      return 'Hello, and welcom to this server!'
   
   app.run(debug=True, host='0.0.0.0', port=serverPort)
