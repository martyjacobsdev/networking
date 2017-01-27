#!/usr/bin/python

################
# Host Distance 
# Finds the physical distance between two host machines
################

from math import radians, cos, sin, asin, sqrt
from urllib2 import urlopen
import socket, json, urllib2

host = raw_input("Enter a hostname: ")
try:
    target_ip = socket.gethostbyname(host)
except:
    print 'Please check the hostname provided.'

my_ip = urlopen('http://ip.42.pl/raw').read()
target_ip_lat_lng = [0,0]
my_lat_lng = [0,0]

def get_target_latlng():

    url = 'http://freegeoip.net/json/' + target_ip 
    response = urllib2.urlopen(url).read()
    data = json.loads(response)
    print '\nHost location: ' + data['region_name'] + ', ' + data['city'] + '.'
    target_ip_lat_lng[0] = data['latitude']
    target_ip_lat_lng[1] = data['longitude']

def get_my_latlng():

    url = 'http://freegeoip.net/json/' + my_ip 
    response = urllib2.urlopen(url).read()
    data = json.loads(response)
    my_lat_lng[0] = data['latitude']
    my_lat_lng[1] = data['longitude']

# haversine formula
def calculate_distance(lon1, lat1, lon2, lat2):
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r

def print_result():

    print '\nThe distance between your machine ' + 'and the target machine ' +  'is approximately: \n' + str(calculate_distance(my_lat_lng[1], my_lat_lng[0], target_ip_lat_lng[1], target_ip_lat_lng[0])) + ' kilometres.'
    

if __name__ == "__main__":
    
    get_target_latlng()
    get_my_latlng()
    print_result() 
