import requests
import pandas as pd
API_URL = "https://statsapi.web.nhl.com/api/v1"
short_API = "https://statsapi.web.nhl.com"
response = requests.get(API_URL + "/teams/23/roster", params={"Content-Type": "application/json"})
data1 = response.json()
#this is the complete data pulled
#print(data1)
persons = (data1["roster"])
#print(persons[0]['person']['fullName'])
df = pd.DataFrame()
#print(persons[0])
Player = []
link = []
position = []
for x in range(len(persons)):
    player = persons[x]
    info = player["person"]
    name = info['fullName']
    if player['position']['code'] == 'G':
        continue
    link.append(info['link'])
    Player.append(name)
    position.append(player['position']['code'])
df['Player'] = Player
df['Link'] = link
df["Position"] = position
df["Goals"] = ''
df["Assists"] = ""
df["Games"] = ''
#print(df.loc[df["Player"] == "Elias Pettersson"])

#print(df["Link"][3])

#for x in (len(df)):
#    response1 = requests.get(short_API + (df["Link"][x]), params={"Content-Type": "application/json"})
#    data1 = response.json()

def sts(x, type_points):
    response1 = requests.get(short_API + (df["Link"][x]) + '/stats?stats=statsSingleSeason&season=20222023', params={"Content-Type": "application/json"})
    data2 = response1.json()
    statys = (data2['stats'][0])
    return (statys['splits'][0]['stat'][type_points])

for x in range(len(df)):
    df["Goals"][x] = sts(x, 'goals')
    df["Assists"][x] =  sts(x, 'assists')
    df["Games"][x] = sts(x, 'games')
df["Points"] = df.Goals + df.Assists
df1 = df.drop('Link', axis=1)
print(df1)

nucks_stats = df1