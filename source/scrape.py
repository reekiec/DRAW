import urllib.request as request
import json

base_url = "https://api.pushshift.io/reddit/search/comment/?q="

def get_json_data(base_url, query):
    api_query = base_url + query
    with request.urlopen(api_query) as response:
        if response.getcode() == 200:
            source = response.read()
            json_data = json.loads(source)
        else:
            return response.getcode()
    return json_data

print(len(get_json_data(base_url, "BTC")["data"]))