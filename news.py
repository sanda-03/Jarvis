import requests
newsapi="e8c20fb903df4f53996b5c6264820043"
r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
data=(r.json())["articles"]
headlines=[article['title'] for article in data]
content=[article['content'] for article in data]
print('\n'.join([str(h) for h in headlines]))
# print('\n'.join([str(c) for c in content]))



