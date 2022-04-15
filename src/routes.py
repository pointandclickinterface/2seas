from email.mime import image
from turtle import title
from flask import Flask, render_template
import sqlite3
import json

#functions
def startdb():
    con=sqlite3.connect('test.db')


def getCountries():
    con = sqlite3.connect('country.db')
    cur = con.cursor()
    all_countries = cur.execute('select country from countries').fetchall()
    country_array= list(map(lambda x: x[0] , all_countries))
    return country_array

#flask routing
app= Flask(__name__, static_url_path="/static")

@app.route("/")
def conn():
    countries=json.dumps(getCountries())
    return render_template('index.html', the_title='2seas', countriesList=countries)

@app.route("/<country>")
def path(country):
    print(country)
    imageLink= "{{ url_for('static',filename='images/SVG/SVG/"+country+".svg') }}"
    print(imageLink)
    return render_template("country.html", the_title=country, image_src=imageLink)

@app.route("/404")
def errors():
    return("error 404")



if __name__ == "__main__":
    startdb()
    app.run()