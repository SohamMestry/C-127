from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = ("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
wiki = requests.get(START_URL)
#.text coverts to string format
soup = BeautifulSoup(wiki.text, "html.parser")
sun_data = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
#The rstrip() method removes any characters (characters at the end a string), 
#space is the default trailing character to remove. here i.text.rstrip() rempves spaces between them
    row = [i.text.rstrip() for i in td]
    sun_data.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(sun_data)):
    name.append(sun_data[i][1])
    distance.append(sun_data[i][3])
    mass.append(sun_data[i][5])
    radius.append(sun_data[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")