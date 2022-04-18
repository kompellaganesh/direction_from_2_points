from requests import request
from flask import request
from services.Directions import Directions
def route():
    try:
        Request = request.json
        srcLat = Request['origin']['Latitude']
        srcLng = Request['origin']['Longitude']
        dstLat = Request['destination']['Latitude']
        dstLng = Request['destination']['Longitude']
        Directionsobject=Directions(srcLat,srcLng,dstLat,dstLng)
        response = Directionsobject.IdentifyRoute()
        return response
    except:
        return "some error",500