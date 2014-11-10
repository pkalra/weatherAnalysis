import urllib3
import json

http = urllib3.PoolManager()

#register to wunderground and get the key for yourself
key='fd27706e9098d47d'

#Get current temperature

# In below url string, replace 'NY' with the state of city and 'New_York' with city of interest (spaces replaced by '_')
r=http.request('GET', 'http://api.wunderground.com/api/'+ key +'/geolookup/conditions/q/NY/New_York.json')
json_string=r.data.decode('utf8')

parsed_json=json.loads(json_string)

#Open the url string in web browser. There are lot of tags available. select the ones you need. I have selected 'location','city',temp_f'
#Example url strings - 
#http://api.wunderground.com/api/fd27706e9098d47d/geolookup/conditions/q/NY/New_York.json
#http://api.wunderground.com/api/fd27706e9098d47d/geolookup/conditions/q/CA/San_Francisco.json
location=parsed_json['location']['city']
temp_f=parsed_json['current_observation']['temp_f']

#weather icon (Sunny,cloudy etc) is available  in icon_url tag. Feel free to try different available tags in url string
print("Current temperature in %s is %s "%(location, temp_f))


#Get historical data for a given date
hist_r=http.request('GET', 'http://api.wunderground.com/api/'+ key +'/history_20131110/q/NY/New_York.json')
hist_json_string=hist_r.data.decode('utf8')
hist_parsed_json=json.loads(hist_json_string)
hist_avg_temp_f=hist_parsed_json['history']['dailysummary'][0]['meantempi']

print("Temperature last year is %s "%(hist_avg_temp_f))
