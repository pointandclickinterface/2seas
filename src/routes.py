from flask import Flask, render_template
import sqlite3

#functions
def startdb():
    con=sqlite3.connect('test.db')


#flask routing
app= Flask(__name__)

@app.route("/")
def conn():
    return render_template('index.html', the_title='2seas')

if __name__ == "__main__":
    startdb()
    app.run()