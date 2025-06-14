import requests #pip install requests

query = input("What type of news are you looking for? ")
api_key = "9df065e385da418f8073d97345ea806d"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-14&sortBy=publishedAt&apiKey={api_key}"
print(url)

r=requests.get(url)
data=r.json()
articles = data['articles']

for index, article in enumerate(articles):
    print(index+1, article['title'] , article['url'])
    print("\n--------------------------------------------------\n")