import requests
import urllib.request
file_path = './nwxjj/'

def get_article(article_id):
	r = requests.get("https://api.kofuf.com/api/articles/%d.json"%article_id, 
		headers = {'from': '2',
		           'version': '3.2.2',
		           'User-Agent': 'ios/iphone7/3.2.2', 
		           'gid':'1047700204', 
		           'token':'3681fc25658447fd9d1423307695c182'})
	data = r.json()
	return {'name': data['name'], 'audio': data['banner']}

articles_respond = requests.get('https://api.kofuf.com/api/channels/7732.json')
article_data = articles_respond.json()

articles = article_data['articles']
article_ids = []
article_items = []

for article in articles:
	item = get_article(article['id'])
	url = item["audio"]
	file_name = file_path + item["name"] + '.mp3'
	print(file_name, url)
	urllib.request.urlretrieve(url, file_name)
