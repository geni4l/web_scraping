import requests

url = 'https://unsplash.com/napi/search?query=owl&per_page=20&xp=feedback-loop-v2:experiment'

r = requests.get(url)

data = r.json()

for item in data['photos']['results']:
	name = item['id']
	url = item['urls']['thumb']
	with open(name+".jpg","wb") as f:
		f.write(requests.get(url).content)

