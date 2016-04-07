#!/usr/bin/env python
# encoding: utf-8
 
import os
import teslajson

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

#Get the array of current data for the car name passed - performs 1 rest call per request
vehicle_data = get_car_data(c, TESLA_CAR_NAME, "vehicle_state")
charge_data = get_car_data(c, TESLA_CAR_NAME, "charge_state")
drive_data = get_car_data(c, TESLA_CAR_NAME, "drive_state")
climate_data = get_car_data(c, TESLA_CAR_NAME, "climate_state")
gui_data = get_car_data(c, TESLA_CAR_NAME, "gui_settings")

print 'Basic Car Data, id, vin etc.\n---------'
for a in c.vehicles:
	for b in a:
		print b + ' : ' + str(a[b])

"""Print some stuff out"""
print_info('Vehicle Data', vehicle_data);
print_info('Charge Data', charge_data);
print_info('Drive State Data', drive_data);
print_info('Climate Data', climate_data);
print_info('GUI Data', gui_data);

#What is the estimated remaining range
print '\n\nSample Particular Output\n-------------------'
print "Est_battery_range=" + str(charge_data["est_battery_range"])
print "Managed User Start Time=" + str(charge_data["managed_charging_start_time"])

""" Commented out for now
#Commands to try
#Set Standard 80% charge rate
#issue_command(c, TESLA_CAR_NAME, "charge_standard")
#Set max 100% charge rate
#issue_command(c, TESLA_CAR_NAME, "charge_max_range")
"""
