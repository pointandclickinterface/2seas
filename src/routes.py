from flask import Flask
import sqlite3

#functions
def startdb():
    con=sqlite3.connect('test.db')


#flask routing
app= Flask(__name__)

@app.route("/")
def conn():
    return "Connected Properly"

if __name__ == "__main__":
    startdb()
    app.run()