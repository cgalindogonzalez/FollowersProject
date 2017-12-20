import requests
from lxml import html


url = 'https://www.instagram.com/foofighters/'
# Get the source code of the chosen instagram account
response = requests.get(url)

# Return the content of the website in a parsed lxml format
tree = html.fromstring(response.text)

# get the value of the followers
path = '//*[@id="react-root"]/section/main/article/header/section/ul/\
li[2]/a/span'
followers_number = tree.xpath(path)

print(followers_number)
