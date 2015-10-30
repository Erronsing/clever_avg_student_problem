import requests
import json

student_Amount = 0.00
section_Amount = 0.00

district_request = requests.get('https://api.clever.com/v1.1/districts/', 
	headers={'Authorization':'Bearer DEMO_TOKEN'})
parsed_districts  = json.loads(district_request.text)['data']

for district in parsed_districts:
	district_uris = [district['uri']]

for district_uri in district_uris:
	print "Uri: {}".format(district_uri)
	section_request = requests.get('https://api.clever.com{}/sections'.format(district_uri), headers = {'Authorization':'Bearer DEMO_TOKEN'})
	parsed_sections = json.loads(section_request.text)['data']
	for section in parsed_sections:
		student_Amount += len(section['data']['students'])
	section_Amount += len(parsed_sections)

average_students = student_Amount/section_Amount
print "Average number of students: {}".format(average_students, '.2f')


