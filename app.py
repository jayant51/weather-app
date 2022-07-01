import asyncio
import urllib.parse
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os

  
# creating the flask app
app = Flask(__name__)
CORS(app) 
# creating an API object
api = Api(app)
  
async def init():
    return('Weather Api init')

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    address = 'Washington DC'
    client = python_weather.Client(format=python_weather.IMPERIAL)
    wresponse="Weather Forecast\n"
    # fetch a weather forecast from a city
    weather = await client.find(address)
    print(address)
     # returns the current day's forecast temperature (int)
    wresponse += "current Temp = "+ str(weather.current.temperature) + "degF\n" 

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        wresponse += "forecast on date = " + str(forecast.date)  + " " +  forecast.sky_text + " " + str(forecast.temperature)+ "degF\n"

    print(wresponse)

    returnurl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(returnurl).json()
    wresponse += address
    wresponse += "Lattitude = " + response[0]["lat"]
    wresponse += "longitude = " + response[0]["lon"]
    # close the wrapper once done
    await client.close()
    return response
  
# Corresponds to POST request
def post(self):
    data = request.get_json(force=True)
    return jsonify({'data': data}), 201
    #return data

# adding the defined resources along with their corresponding urls
#api.add_resource(getweather, '/weather')
#api.add_resource(init, '/')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

