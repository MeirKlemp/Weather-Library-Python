
'''
This module has the object "Location".
The purpose of the object is to present a location to get its weather by the module "weather".
'''

from weather_exeptions import FindLocationError
from json import loads

# Loads all the locations from the JSON file city.list.json.
locations = loads(open('city.list.json', 'r', encoding='utf8').read())


class Location:
    '''
    Specific location in the world to find its weather.
    '''
    @staticmethod
    def getlocations(**data): # O(n), n is all the locations.
        '''
        Gets a list of locations with the data from the parameters.
        '''
        if data:
            global locations
            locs = []

            for loc in locations:
                if 'id' in data:
                    if data['id'] != loc['id']:
                        continue
                if 'city' in data:
                    if data['city'].lower() not in loc['name'].lower():
                        continue
                if 'country' in data:
                    if data['country'].lower() not in loc['country'].lower():
                        continue
                if 'lon' in data:
                    if data['lon'] != loc['coord']['lon']:
                        continue
                if 'lat' in data:
                    if data['lat'] != loc['coord']['lat']:
                        continue
                locs.append(Location(loc['id']))
            return locs

    def __init__(self, id): # O(n), __getdata() = O(n).
        '''
        id to locate the locations.
        In order to find location with other details, the static function getlocations() will do the work.
        '''
        self.id = id
        self.__getdata()

    def __getdata(self): # O(n), n is all the locations.
        '''
        Gets all the data of the location by the id.
        '''
        for loc in locations:
            if self.id == loc['id']:
                self.country = loc['country']
                self.city = loc['name']
                self.lon = loc['coord']['lon']
                self.lat = loc['coord']['lat']
                return True
        raise FindLocationError('Cannot find the ID in the file \'city.list.json\'')

    def __str__(self): # O(1)
        return '\n'.join('{0}: {1}'.format(key, value) for key, value in vars(self).items())