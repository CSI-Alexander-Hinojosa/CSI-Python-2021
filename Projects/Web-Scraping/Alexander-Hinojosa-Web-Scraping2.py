import requests
res = requests.get("https://www.gutenberg.org/files/1661/1661-0.txt")
res.raise_for_status()
playFile= open("The Adventures of Sherlock Holmes.text", "wb")
for chunk in res.iter_content(555725):
    playFile.write(chunk)
playFile.close()