# we will grab some data from the internet then examine it
import requests # we might need to pip install requests

def getPhotos(): # API means Application Programming Interface (get data from an api)
    '''Make a request to an API then present the data nicely'''
    # we need to remember the URL where the data lives
    api = 'https://jsonplaceholder.typicode.com/photos'
    # and we need a structure to store the returned data
    response = requests.get(api)
    # usually, API data is formatted as JSON
    response_list = response.json() # Python will automatically convert the JSON to a list
    return response_list

# we can call our function
photos = getPhotos() # photos is a list of dictionaries
# we can take a look at just the zero-th member of the data
print( photos[0], type(photos[0]) )