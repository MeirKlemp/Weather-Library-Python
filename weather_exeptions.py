'''
The module has the exeptions "WeatherRequestError" and "FindLocationError".
The purpose of the objects is to display the error to the user.
'''

class WeatherRequestError(Exception):
    '''
    This exeption occurs when the request to the server has errors.
    '''
    pass
class FindLocationError(Exception):
    '''
    This exeption occurs when the location cannot be found.
    '''
    pass