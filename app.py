import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
  return "Welcome to my Demo Web-app HOME page"

@app.route("/fish")
def fishing():
  return "----~~~---- Slow fishing!!..."

if __name__ == "__main__":
  app.run()
 
