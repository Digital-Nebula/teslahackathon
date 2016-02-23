#!/usr/bin/env python
# encoding: utf-8
 
import os
import teslajson
 
TESLA_EMAIL = os.environ['TESLA_EMAIL']
TESLA_PASSWORD = os.environ['TESLA_PASSWORD']

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

#---------Main Flow------------ 
#Connect to the car (using credentials in environment)
c = establish_connection()

#Get the array of current data for the car (vehicle and charge state)
vehicle_data = get_car_data(c, "Blue Thunder", "vehicle_state")
charge_status = get_car_data(c, "Blue Thunder", "charge_state")

#Get the api list of commands (currently supported)
#print "Vehicle State Data:\n" + "\n".join(vehicle_data)
#print "Charge State Commands:\n" + "\n".join(charge_status)

#Lets print a few things
print "Mileage=" + str(vehicle_data["odometer"])
print "Is Locked?=" + str(vehicle_data["locked"])

#What is the estimated remaining range
print "Est_battery_range=" + str(charge_status["est_battery_range"])
#EU Vehicle query
print "EU Vehicle=" + str(charge_status["eu_vehicle"])
print "Managed User Start Time=" + str(charge_status["managed_charging_start_time"])

#Commands to try
#Set Standard 80% charge rate
#issue_command(c, "Blue Thunder", "charge_standard")
#Set max 100% charge rate
#issue_command(c, "Blue Thunder", "charge_max_range")
