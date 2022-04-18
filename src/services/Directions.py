import requests
from turfpy.measurement import along
from geojson import LineString
from config import  config

class Directions:
    def __init__(self,srcLat,srcLng,dstLat,dstLng):
        self.srcLat=srcLat
        self.srcLng=srcLng
        self.dstLat=dstLat
        self.dstLng=dstLng
    def IdentifyRoute(self):
        URL = config.configurations['MapsAPI']['URL']
        APIKEY = config.configurations['MapsAPI']['APIKEY']
        resp=requests.get(('{}?key={}&mode=walking&destination={},{}&origin={},{}').format(URL,APIKEY,self.dstLat,self.dstLng,self.srcLat,self.srcLng))
        mapsapiresp= resp.json()
        steps = mapsapiresp['routes'][0]['legs'][0]['steps']
        totalDistance=0
        ls=[[steps[0]['start_location']['lng'],steps[0]['start_location']['lat']]]
        path=[[steps[0]['start_location']['lat'],steps[0]['start_location']['lng']]]
        for step in steps:
            totalDistance+=step['distance']['value']
            ls.append([step['end_location']['lng'],step['end_location']['lat']])
        linestring = LineString(ls)
        count = int(totalDistance/50)
        for i in range(count):
            pointfeature=(along(linestring,50*(i+1),'m'))
            if pointfeature['geometry']['coordinates'][::-1]!=path[-1]:
                path.append(pointfeature['geometry']['coordinates'][::-1])
        if path[-1]!=ls[-1][::-1]:
            path.append(ls[-1][::-1])
        responsestring=""
        for coord in path:
            responsestring+=str(coord[0])+','+str(coord[1])+',\n'
        return responsestring