#!/usr/bin/env python
# encoding: utf-8
 
import os
import teslajson
import datetime

#--------Setup vars---------
TESLA_EMAIL = os.environ['TESLA_EMAIL']
TESLA_PASSWORD = os.environ['TESLA_PASSWORD']
TESLA_ACCESS_TOKEN = os.environ['TESLA_ACCESS_TOKEN']
TESLA_CAR_NAME = os.environ['TESLA_CAR_NAME']

#-------Helper Functions------------ 
def establish_connection(token=None):
    c = teslajson.Connection(email=TESLA_EMAIL, password=TESLA_PASSWORD, access_token=token)
    return c

def get_car_data(c, car, request):
    for v in c.vehicles:
       if v["display_name"] == car:
          d = v.data_request(request)
	  return d

def issue_command(c, car, comm):
    for v in c.vehicles:
       if v["display_name"] == car:
          d = v.command(comm)
	  return d

def print_info(name, data):
	print '\n\n' + name + '\n-----------------------------'
	for x in data:
		print x + ' : ' + str(data[x])
	return 0

#---------Main Flow------------ 
#Connect to the car (using credentials in environment)
c = establish_connection(TESLA_ACCESS_TOKEN)
f = open('/tmp/outputfiledata','a')

#Get the array of current data for the car (vehicle and charge state)
drive_data = get_car_data(c, TESLA_CAR_NAME, "drive_state")

def print_info(name, data, fhan):
        fhan.write((datetime.datetime.fromtimestamp(data['gps_as_of']).strftime('%d-%m-%Y %H:%M:%S')) +','+ str(data['speed']) + ',' + str(data['longitude']) + ','+ str(data['latitude']) + ',' + str(data['shift_state']) + ',' + str(data['heading']) +'\n')

"""Print some stuff out"""
print_info('Drive State Data', drive_data, f);
