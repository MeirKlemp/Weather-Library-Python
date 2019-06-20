
'''
This module is a command line interface to get the weather of locations.

The module is an example of the usage that can be made from the module "weather".
'''

from weather import getweather, Location, Weather
import re


class CommandError(Exception):
    '''
    This exeption occurs when a command in the CLI has been writed false.

    The exeption gives also the command with the bad usage.
    '''
    def __init__(self, message, command): # O(1)
        '''
        message is the error that will display to the user.

        command is the command with the bad usage.
        '''
        super().__init__(message)
        self.command = command

def orderargs(*args): # O(m*n=n^2), n is the amount of the amount of values in list, m is the amount of values in tuples.
    '''
    Converts the user's input to a dict with the args.

    args is a list of tuples: [('arg', 'value(or '')', 'value(or '')' ...), ...].
    '''
    dictargs = {}
    for arg in args:
        dictargs[arg[0]] = [i for i in arg[1:] if i][0]
    return dictargs

def locations(**args): # O(n), n is the getlocations complexity.
    '''
    Commits the command "locations".

    args is a dict with args and values.
    '''
    if all(keys not in ['id', 'city', 'country', 'lon', 'lat'] for keys in args):
        raise CommandError('Wrong arguments', 'locations')
    locations = Location.getlocations(**args)
    return '\n{0}\n'.format('#' * 15).join(str(loc) for loc in locations)

def weather(**args): # O(n), n is the getweather complexity.
    '''
    Commits the command "weather".

    args is a dict with args and values.
    '''
    if all(keys not in ['id', 'units'] for keys in args):
        raise CommandError('Wrong arguments', 'weather')
    return getweather(Location(int(args['id'])), units=args['units'] if 'units' in args else 'c')

def gethelp(**args): # O(n), n is the amount of commands to display its usage.
    '''
    Commits the command "help".

    args is a dict with args and values.
    '''
    global commands
    printcoms = {}

    if args:
        for key in sorted(args):
            if not key.isdigit():
                raise CommandError("'%s' is not an integer, index must be an integer" % key, 'gethelp')
            printcoms[key] = '{0}: {1}'.format(args[key], commands[args[key]][1])
    else:
        printcoms['Syntax'] = '<Command> <arg 1> = <value> <arg 2> = <value> ..., <arg n> = <value>'
        for key, value in commands.items():
            printcoms[key] = value[1]


    return '\n'.join('{0}: {1}'.format(com, des) for com, des in printcoms.items())

def version(**args): # O(1)
    '''
    Commits the command "version".

    Doesn't use the parameter args.
    '''
    return 'Version: 1.0'

# Command : [Function, Description] 
commands = {'locations' : [locations, 'Get all locations with arguments, args: id = <number> country = <value> city = <value> lon = <longitude> lat = <latitude>'],
            'weather': [weather, 'Get weather live byse location id, args: id = <number> units = <c: Celsius(Default), f: Fahrenheit, any: Kelvin>'],
            'help': [gethelp, 'Show help, args: <index> = <command>'],
            'version': [version, "Show the program's version"],
            'exit': [None, 'Close the program']}
# Patterns for regular expression.
patterncmd = r'^\s*(\w+)'
patternargs = r'''\W+(\w+)\s*=\s*(?:(\w+)|(?:\"(.*)\"|'(.*)'))'''

if __name__ == "__main__":
    command = input('weather > ').lower()

    while command != 'exit':
        if command:
            try:
                args = re.findall(patternargs, command)
                command = re.search(patterncmd, command).group(1)
                print(commands[command][0](**orderargs(*args)))
            except KeyError:
                print('Unknown command', 'Enter \'help\' to see all the available commands', sep='\n')
            except CommandError as ce:
                print(ce, gethelp(**{'0': ce.command}), sep='\n\n')
            except Exception as e:
                print (e)
        command = input('weather > ').lower()