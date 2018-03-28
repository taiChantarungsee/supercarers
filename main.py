#!/usr/bin/env python
import logging, time, json, math

from flask import Flask, jsonify, make_response

app = Flask(__name__)

logging.basicConfig(filename='log.txt', level=logging.ERROR)

with open('forecast.json') as file:
	data = json.load(file)

#url for quering specific fields
@app.route('/weather/london/<date>/<time>/', methods=['GET'])
@app.route('/weather/london/<date>/<time>/<property>/', methods=['GET'])
def get_weather_by_property(date, time, property=None):
	try:
		info = data['list']
		for entry in info:
			date_time = entry['dt_txt'].split(' ')
			date_text = date_time[0].replace('-', '')
			time_text = date_time[1].replace(':', '')[:-2]
			if date_text == date and time_text == time:
				answer_dict = {'description': entry['weather'][0]['description'],
						'temperature': str(math.ceil((entry['main']['temp'] - 32.0)*5.0/9.0)) + 'c',
						'pressure': str(entry['main']['pressure']),
						'humidity': str(entry['main']['humidity']) + '%',}
				if property:
					answer = {property: answer_dict[property]}
				else:
					answer = answer_dict 
				return jsonify(answer)
	except KeyError as e:
			print ('Error code:', e)
			#log the error
			logging.exception('Error getting weather data.')
			return
	return make_response(jsonify({'status': 'error', 'message': f"No data for {date} {time}"}), 404)

if __name__ == '__main__':
	print("Server has started!")
	app.run(host='0.0.0.0', port=80)
