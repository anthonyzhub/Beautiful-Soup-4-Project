#! /usr/bin/python3

# Source: https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_souping_the_page.htm

from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# Extract webpage's title
print(soup.title)

# Print all URL links on the webpage
for i in soup.find_all("a"):
    print(i.get("href"))