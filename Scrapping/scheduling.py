from datetime import datetime
import json
import urllib.request

data = [
  {
    'place_id': 'ChIJfVpQRQq_woARQ5hwJsast6s',
    'name': 'Hollywood Sign',
    'address': 'Los Angeles, CA 90068, USA',
    'latitude': 34.1341151,
    'longitude': -118.3215482,
    'rating': 4.5,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 3456,
        'width': 5184,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/116376707004950173811/photos">A Google User</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJBTk8wjy5woARmunGKGJ3PCI',
    'name': 'Public Art "Urban Light"',
    'address': '5905 Wilshire Blvd, Los Angeles, CA 90036, USA',
    'latitude': 34.0630235,
    'longitude': -118.3592373,
    'rating': 4.6,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 3036,
        'width': 4048,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/112475486629041102698/photos">Michael Ferguson</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJ9590IY3AwoARquS6ie60MUc',
    'name': 'Griffith Park',
    'address': '4730 Crystal Springs Dr, Los Angeles, CA 90027, USA',
    'latitude': 34.13655440000001,
    'longitude': -118.2942,
    'rating': 4.7,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 3261,
        'width': 4905,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/115132742270239745397/photos">Prateek Raghuwanshi</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJgeTONsK-woARwI4tqLroLnI',
    'name': 'Roadside Attractions LLC',
    'address': '7920 Sunset Blvd, Los Angeles, CA 90046, USA',
    'latitude': 34.097532,
    'longitude': -118.362598,
    'rating': 4.1,
    'open_hour': '12:00',
    'close_hour': '6:00',
    'url': '',
    'photos': [
      
    ]
  },
  {
    'place_id': 'ChIJgQpEAUXGwoARoG9LzK0GhV0',
    'name': 'El Pueblo de Los Angeles Historical Monument',
    'address': '125 Paseo De La Plaza, Los Angeles, CA 90012, USA',
    'latitude': 34.0567217,
    'longitude': -118.2384286,
    'rating': 4.4,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 960,
        'width': 1280,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/115862629829929880484/photos">Alberto Gozzelino</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJl7OFCzfGwoARZYJhjm93dIg',
    'name': 'Little Tokyo',
    'address': '319 E 2nd St #202, Los Angeles, CA 90013, USA',
    'latitude': 34.0493433,
    'longitude': -118.2396309,
    'rating': 4.5,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 2952,
        'width': 5248,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/114142941435967850952/photos">Muhrr Duhh</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJS-OwJN3HwoARHEGQWoH2fb4',
    'name': 'Public Art "The Intimacy of Place"',
    'address': 'Station Platform, 2460 S Flower St, Los Angeles, CA 90007, United States',
    'latitude': 34.0293657,
    'longitude': -118.273467,
    'rating': 5,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 1299,
        'width': 1413,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/114869409171934317910/photos">Public Art in Public Places</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJI56cmyO_woAR5--6TZV6Z3I',
    'name': 'Hollywood Wax Museum®',
    'address': '6767 Hollywood Blvd, Los Angeles, CA 90028, USA',
    'latitude': 34.10173109999999,
    'longitude': -118.3381527,
    'rating': 4.3,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 3024,
        'width': 4032,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/107638415428758561001/photos">A Google User</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJ0xG7n03GwoARsDH_OyyMcrM',
    'name': 'Walt Disney Concert Hall',
    'address': '111 S Grand Ave, Los Angeles, CA 90012, USA',
    'latitude': 34.0553454,
    'longitude': -118.249845,
    'rating': 4.7,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 567,
        'width': 850,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/101360285840845819302/photos">Thelma Polanco-Perez</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJDZLWjSO_woARw_jlzAQ3al0',
    'name': 'Discover Los Angeles Visitor Information Center (Hollywood)',
    'address': 'Hollywood & Highland, 6801, Hollywood Blvd, Los Angeles, CA 90028, United States',
    'latitude': 34.1024501,
    'longitude': -118.3399853,
    'rating': 4.3,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 3024,
        'width': 4032,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/111447386696558481102/photos">Albert Landicho</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJk1R_FwO_woARGMOiMiXmMwU',
    'name': 'Jerome C. Daniel Overlook above the Hollywood Bowl',
    'address': '7036 Mulholland Dr, Los Angeles, CA 90068, USA',
    'latitude': 34.116428,
    'longitude': -118.3421476,
    'rating': 4.5,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 1536,
        'width': 2048,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/115643750450873007125/photos">Klaus Blaschke</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJJYpUmiO_woAR9EnZqq2vgnM',
    'name': 'Guinness World Records Museum',
    'address': '6764 Hollywood Blvd, Los Angeles, CA 90028, USA',
    'latitude': 34.1014015,
    'longitude': -118.3380435,
    'rating': 3.7,
    'open_hour': '12:00',
    'close_hour': '6:00',
    'url': '',
    'photos': [
      {
        'height': 1152,
        'width': 2048,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/108652857526062496371/photos">Guinness World Records Museum</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJodIfJFrGwoARLdxWbyjLv8g',
    'name': 'Chinatown Central Plaza',
    'address': '943 N Broadway, Los Angeles, CA 90012, USA',
    'latitude': 34.065245,
    'longitude': -118.2374264,
    'rating': 4.1,
    'open_hour': '12:00',
    'close_hour': '6:00',
    'url': '',
    'photos': [
      {
        'height': 2229,
        'width': 3301,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/106644922901975237663/photos">Virtual Cat</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJC8ClADc23YARGv3mnzwNeu0',
    'name': 'LA Waterfront',
    'address': '600 Sampson Way, San Pedro, CA 90731, USA',
    'latitude': 33.738759,
    'longitude': -118.279002,
    'rating': 4.5,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 3024,
        'width': 4032,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/100234448685271542135/photos">Andy Ackley</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJVfNmkUrGwoARwl2Dn8e8CYA',
    'name': 'Destination Downtown LA Tours',
    'address': '541 S Spring St #307, Los Angeles, CA 90013, USA',
    'latitude': 34.0466219,
    'longitude': -118.2507019,
    'rating': 4.8,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 1647,
        'width': 2307,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/116702330655219021556/photos">Destination Downtown Los Angeles</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJdZbSPDg23YAR6yR-akC2g4E',
    'name': 'Battleship USS Iowa Museum',
    'address': '250 S Harbor Blvd, Los Angeles, CA 90731, USA',
    'latitude': 33.7422615,
    'longitude': -118.2772823,
    'rating': 4.7,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 628,
        'width': 1200,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/109608436745432719096/photos">Battleship USS Iowa Museum</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJhX1uVuC-woARQNzq4-b1Prk',
    'name': 'Runyon Canyon Park',
    'address': '2000 N Fuller Ave, Los Angeles, CA 90046, USA',
    'latitude': 34.1052437,
    'longitude': -118.3489574,
    'rating': 4.7,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 1362,
        'width': 2048,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/107784807394608276081/photos">Jeremy Murphy</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJY-otQbHHwoARFLxG5thhkC4',
    'name': 'Go Los Angeles® Card',
    'address': '6801 Hollywood Blvd, Los Angeles, CA 90028, USA',
    'latitude': 34.1018654,
    'longitude': -118.3393568,
    'rating': 4.5,
    'open_hour': '11:00',
    'close_hour': '6:30',
    'url': '',
    'photos': [
      {
        'height': 2268,
        'width': 4032,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/109437499817447957637/photos">Murty Govindu Sridhara Sudharshana</a>'
        ]
      }
    ]
  },
  {
    'place_id': 'ChIJywjU6WG_woAR3NrWwrEH_3M',
    'name': 'Griffith Observatory',
    'address': '2800 E Observatory Rd, Los Angeles, CA 90027, USA',
    'latitude': 34.1184341,
    'longitude': -118.3003935,
    'rating': 4.7,
    'open_hour': '10:00',
    'close_hour': '8:00',
    'url': '',
    'photos': [
      {
        'height': 1333,
        'width': 2000,
        'htmllink': [
          '<a href="https://maps.google.com/maps/contrib/115694673842827640801/photos">Müge Nötzli</a>'
        ]
      }
    ]
  }
]

# data = data.encode('utf-8')

for i in range(len(data)):
	try:
		del data[i]['url']
		# del data[i]['place_id']
	except:
		pass

	start = int(data[i]['open_hour'].split(":")[0]) + int(data[i]['open_hour'].split(":")[1])/30.0
	end = int(data[i]['close_hour'].split(":")[0]) + int(data[i]['close_hour'].split(":")[1])/30.0
	if start > end:
		end += 12
	data[i]['burst_time'] = (end - start)
    
sorted_data_arriv = sorted(data, key=lambda data: int(data['open_hour'].split(':')[0])) 

for j in range(len(sorted_data_arriv)-1):
	if (int(sorted_data_arriv[j]['open_hour'].split(':')[0])*60 + int(sorted_data_arriv[j]['open_hour'].split(':')[1])) == (int(sorted_data_arriv[j+1]['open_hour'].split(':')[0])*60 + int(sorted_data_arriv[j+1]['open_hour'].split(':')[1])):
		if (sorted_data_arriv[j]['burst_time']) > (sorted_data_arriv[j+1]['burst_time']):
			temp = sorted_data_arriv[j+1]
			sorted_data_arriv[j+1] = sorted_data_arriv[j]
			sorted_data_arriv[j] = temp
		elif (sorted_data_arriv[j]['burst_time']) == (sorted_data_arriv[j+1]['burst_time']):
			if sorted_data_arriv[j]['rating'] < sorted_data_arriv[j+1]['rating']:
				temp1 = sorted_data_arriv[j+1]
				sorted_data_arriv[j+1] = sorted_data_arriv[j]
				sorted_data_arriv[j] = temp1

# print(sorted_data_arriv)
import urllib.parse
dur_tuple = list()
for i in range(len(sorted_data_arriv)-1):
	for j in range(i+1, len(sorted_data_arriv)):
		with urllib.request.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+urllib.parse.quote(sorted_data_arriv[i]['address'])+'&destinations='+urllib.parse.quote(sorted_data_arriv[j]['address'])+'&key=AIzaSyDFdP_s4uJmTv6i06k7uvnR9Urhlnmuk1U') as url:
			data1 = json.loads(url.read().decode())['rows'][0]['elements'][0]['duration']['value']/60.0
			dur_tuple.append([sorted_data_arriv[i]['place_id'], sorted_data_arriv[j]['place_id'], data1])
# print(dur_tuple)
dur_tuple = sorted(dur_tuple, key=lambda dur_tuple: dur_tuple[2])
import math
def add_times(time, duration):
    hours, minutes = int(time.split(":")[0]), int(time.split(":")[1])/60.0
    new_time = (hours+minutes) + duration
    new_hours = math.floor(new_time)
    new_minutes = int(round((new_time - new_hours)*60,2))
    if new_minutes < 10:
        return str(new_hours)+":0"+str(new_minutes)
    else:
        return str(new_hours)+":"+str(new_minutes)

def find_nearest(place_id, dur_tuple, sorted_data_arriv):
    time = 0
    for t in dur_tuple:
        if place_id in t:
            if t.index(place_id) == 0: nearest_id = t[1]
            else: nearest_id = t[0]
            time = t[2]
            for i in range(len(sorted_data_arriv)):
                if sorted_data_arriv[i]['place_id'] == nearest_id:
                    return (sorted_data_arriv[i], time, i)

num_days = 4
duration_ = 2
it = dict()
day_ind = 0
while num_days > 0 and len(sorted_data_arriv) > 0:
    it[day_ind] = {}
    loc_no = 0
    first_of_day = sorted_data_arriv[0]
    day_start = first_of_day['open_hour']
    del sorted_data_arriv[0]
    it[day_ind][loc_no] = {}
    it[day_ind]["closed"] = 1
    it[day_ind][loc_no]["Name"] = first_of_day['name']
    it[day_ind][loc_no]["Reach_by"] = day_start
    it[day_ind][loc_no]["Location"] = {"lat": first_of_day['latitude'], "lng": first_of_day['longitude']}
    it[day_ind][loc_no]["Rating"] = first_of_day['rating']
    it[day_ind][loc_no]["Opening"] = first_of_day['open_hour']
    it[day_ind][loc_no]["Closing"] = first_of_day['close_hour']
    it[day_ind][loc_no]["Leave_by"] = add_times(it[day_ind][loc_no]["Reach_by"], duration_)
    current_time = it[day_ind][loc_no]["Leave_by"]
    nearest_place, time_to_reach, pos = find_nearest(first_of_day['place_id'], dur_tuple, sorted_data_arriv)
    current_time = add_times(current_time, time_to_reach/60.0)
    while int(current_time.split(":")[0]) < 19 and len(sorted_data_arriv) > 0:
        del sorted_data_arriv[pos]
        loc_no += 1
        it[day_ind][loc_no] = {}
        it[day_ind][loc_no]["Name"] = nearest_place['name']
        it[day_ind][loc_no]["Reach_by"] = current_time
        it[day_ind][loc_no]["Location"] = {"lat": nearest_place['latitude'], "lng": nearest_place['longitude']}
        it[day_ind][loc_no]["Rating"] = nearest_place['rating']
        it[day_ind][loc_no]["Opening"] = nearest_place['open_hour']
        it[day_ind][loc_no]["Closing"] = nearest_place['close_hour']
        it[day_ind][loc_no]["Leave_by"] = add_times(it[day_ind][loc_no]["Reach_by"], duration_)
        closing = str(int(nearest_place['close_hour'].split(":")[0])+12)+":"+nearest_place['close_hour'].split(":")[1]
        if it[day_ind][loc_no]["Leave_by"] > closing:
            del it[day_ind][loc_no]
            break
        current_time = it[day_ind][loc_no]["Leave_by"]
        if len(sorted_data_arriv) > 0:
            nearest_place, time_to_reach, pos = find_nearest(nearest_place['place_id'], dur_tuple, sorted_data_arriv)
            current_time = add_times(current_time, time_to_reach/60.0)
        else:
            break
    num_days -= 1
    day_ind += 1

print(it)