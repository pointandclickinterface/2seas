from email.mime import image
from turtle import title
from flask import Flask, render_template
import mysql.connector
import json

#functions
# def startdb():
#     con=sqlite3.connect('test.db')

def getWaterGDP():
    cursor.execute('select * from water_gdp')
    result= cursor.fetchall()

    water_gdp_array= list(map(lambda x: x , result))
    return water_gdp_array

def getregionWaterGDP():
    cursor.execute('select * from world_water_gdp')
    result= cursor.fetchall()

    water_gdp_array= list(map(lambda x: x , result))
    return water_gdp_array

def getCountries():
    cursor.execute('select * from country')
    result= cursor.fetchall()

    country_array= list(map(lambda x: (x[1],x[0]) , result))
    return country_array

def getTargets():
    cursor.execute('select * from sanitation_targets')
    result= cursor.fetchall()

    target_array= list(map(lambda x: x , result))
    return target_array

def getCountryDataSummary(country_id):
    cursor.execute('select * from data_summary where country_id = '+str(country_id))
    result=cursor.fetchall()

    countryDataSummary = list(map(lambda x: x , result))

    return countryDataSummary


#flask routing
app= Flask(__name__, static_url_path="/static")

@app.route("/")
def conn():
    countries=json.dumps(getCountries())
    gdp=json.dumps(getWaterGDP())
    regiongdp=json.dumps(getregionWaterGDP())
    return render_template('index.html', the_title='2seas', countriesList=countries, waterGdp=gdp, regionWaterGdp=regiongdp)

@app.route("/<country>")
def path(country):
    countryList=getCountries()
    countries=json.dumps(countryList)
    for place in countryList:
        tempplace=place[0].replace(" ","_")
        if tempplace == country:
            code=place[1]
        else:
            errors()
    dataSummaryList=getCountryDataSummary(code)
    dataSummary=json.dumps(dataSummaryList)
    targets=json.dumps(getTargets())
    imageLink= "{{ url_for('static',filename='images/SVG/SVG/"+country+".svg') }}"
    return render_template("country.html", the_title=country, image_src=imageLink, countriesList=countries, data_sum=dataSummary, target=targets)

@app.route("/whatcanido/<place>")
def whatcanido(place):
    return(place)

@app.route("/404")
def errors():
    return("error 404")



if __name__ == "__main__":
    # startdb()
    cnx = mysql.connector.connect(user='2seas', password='Waterwater2!',
                                  host='ec2-54-197-15-207.compute-1.amazonaws.com',
                                  database='twoseas')
    cursor= cnx.cursor()
    app.run()
