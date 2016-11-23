import click
import octopart
from downloader import fetch_file

@click.command()
@click.option("--api-key",
	prompt="Your Octopart API key",
	help="The API key used to access the Octopart API")
@click.option("--part",
	prompt="Part number or keywords",
	help="The search query sent to Octopart for finding a datasheet")
@click.option("--all", default=False,
	help="Fetch all associated datasheets instead of just one.")
def fetch(api_key, part, all):
	print("Fetching datasheet for", part)
	results = octopart.search(api_key, part)

	if len(results) == 0:
		print("Sorry! No parts were found for", part)
		return

	datasheets = octopart.get_datasheet_urls(results)

	if len(datasheets) == 0:
		print("Sorry! No datasheets were found for", part)
		return

	if all:
		for d in datasheets:
			fetch_file(d)
	else:
		for d in datasheets:
			if ".pdf" in d:
				fetch_file(d)
				break

if __name__ == "__main__":
	fetch()
