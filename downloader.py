from tqdm import tqdm
import requests
from urllib.parse import urlparse
import os.path

def fetch_file(url):
	response = requests.get(url, stream=True)
	path = urlparse(url).path
	fname = os.path.split(path)[1]

	with open(fname, "wb") as handle:
		for data in tqdm(response.iter_content()):
			handle.write(data)
