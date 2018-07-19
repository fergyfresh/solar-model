import requests
import json
from os import getenv

class PVWattsV6(object):

    def __init__(self, api_key, lat, lon, array_type, tilt,
                 azimuth, module_type, losses, system_capacity,
                 url_seperator="?", parameter_separator="&"):
        self.base_url = 'https://developer.nrel.gov/api/pvwatts/v6.json'
        self.api_key = api_key
        self.format = "JSON"
        self.lat = lat
        self.lon = lon
        self.array_type = array_type
        self.tilt = tilt
        self.azimuth = azimuth
        self.module_type = module_type
        self.losses = losses
        self.system_capacity = system_capacity
        self.url_seperator = url_seperator
        self.parameter_separator = parameter_separator
                 
    def __build_params(self):
        return [
             "api_key=" + self.api_key,
             "format=" + self.format,
             "lat=" + self.lat,
             "lon=" + self.lon,
             "array_type=" + self.array_type,
             "tilt=" + self.tilt,
             "azimuth=" + self.azimuth,
             "module_type=" + self.module_type,
             "losses=" + self.losses,
             "system_capacity=" + self.system_capacity]
              
    def __build_api_url(self):
        return self.base_url + \
               self.url_seperator + \
               self.parameter_separator.join(self.__build_params())

    def get_data(self):
        r = requests.get(self.__build_api_url())
        output = json.loads(r.text)
        if r.status_code == 200:
            return (200, output['outputs'])
        elif r.status_code == 422:
            return (422, "\n".join(output['errors']))


