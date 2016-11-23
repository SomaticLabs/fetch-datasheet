import requests

from urllib.parse import urlencode

base_url = "https://octopart.com/api/v3/parts/search?"

def search(api_key, query):
	params = {
		'apikey': api_key,
		'q': query,
		'include[]': "datasheets"
	}
	query = urlencode(params)

	url = base_url + query

	r = requests.get(url)
	data = r.json()
	results = data['results']

	return results

def get_datasheet_urls(results, all=False):
	result = results[0]
	datasheets = result['item']['datasheets']

	return [d['url'] for d in datasheets]
