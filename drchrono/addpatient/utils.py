def parse_office(response):
  office_details = {}
  for info in response['results']:
    office_details["name"] = info['name']
    office_details["address"] = info['address']
    office_details["city"] = info['city']
    office_details["state"] = info['state']
    office_details["zip_code"] = info['zip_code']

  return office_details



def parse_appointments(response):
  appointments = []
  for timeslots in response['results'][0]['online_timeslots']:
    if timeslots['day'] == 1:
      timeslots['day'] = 'Monday'
    elif timeslots['day'] == 3:
      timeslots['day'] = 'Wednesday'
    else:
      timeslots['day'] = 'Friday'

    appointments.append([timeslots['day'], timeslots['hour']])




  return appointments