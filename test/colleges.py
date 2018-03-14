base_url = 'http://bioguide.congress.gov/scripts/biodisplay.pl?index='

import requests
from bs4 import BeautifulSoup


def yes_no(tag):
	url = base_url + tag
	resp = requests.get(url)
	text = resp.text

	soup = BeautifulSoup(text, 'lxml')

	tags = soup.select('p')

	text1 = tags[0].text

	return "Stanford" in text1

	# if "Stanford" in text1:
	# 	return "YES"
	# else:
	# 	return "No"


ids = ['F000062', 'K000389', 'H001075']

xcount = 0
for i in ids:
	if yes_no(i):
		xcount += 1

print (xcount)