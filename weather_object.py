
'''
This module has the object "Weather".
The purpose of the object is to present a weather of a location by the module "weather".
'''

class Weather:
    '''
    Weather of a specific location, it must have at list the attribute temperature of the location.
    '''
    def __init__(self, temp, **data): # O(n), n is the amount of parameters the function got.
        '''
        Gets a temperature of a location and can get more data of the location.
        '''
        self.temp = temp
        self.__dict__.update(data)

    def __str__(self): # O(n), n is the amount of attributes the object has. of the location.
        return '\n'.join('{0}: {1}'.format(key, value) for key, value in vars(self).items())
