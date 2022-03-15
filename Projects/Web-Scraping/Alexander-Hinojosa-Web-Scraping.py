import requests
res= requests.get("https://www.gutenberg.org/files/76/76-0.txt") 
type(res)
res.status_code == requests.codes.ok

len(res.text)

print(res.text[:300])
