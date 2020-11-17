#followed https://fantasypython.co/ on how to grab data online and input it into a 
#workable dataframe


import requests
import pandas as pd

#function that uses heuristic algorithm to calculate a player's ranking
def calculate(val1, val2):
    if val1 == 0:
        return val2
    elif val2 == 0:
        return val1
    return(val1*.75 + val2*.25)

#expert rankings
r = requests.get('https://partners.fantasypros.com/api/v1/consensus-rankings.php?sport=NFL&year=2020&week=0&id=1054&position=ALL&type=ST&scoring=HALF&filters=7:9:285:699:747&export=json')
#ADP or average draft position by regular fantasy football players
crowds = requests.get('https://fantasyfootballcalculator.com/api/v1/adp/standard?teams=8&year=2020')

value_rank = []
expert_list = []
adp_list = []

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''


for player_name in crowds.json()['players']:
    for ele in player_name:  
        if ele in punc:  
            #remove unwanted punctuation that might accidentally
            #differentiate the same player
            player_name = player_name.replace(ele, "") 
    adp_list.append(player_name['name'])
for player_name in r.json()['players']:
    for ele in player_name:  
        if ele in punc:  
            player_name = player_name.replace(ele, "") 
    expert_list.append(player_name['player_name'])

only_in_adp = set(adp_list) - set(expert_list)
only_in_expert = set(expert_list) - set(adp_list)
total = set(expert_list + adp_list)

for player in total:
    if player in expert_list and player in adp_list:
        for x in r.json()['players']:
            if x['player_name'] == player:
                expert_ranking = x['rank_ecr']
        for y in crowds.json()['players']:
            if y['name'] == player:
                adp_ranking = y['adp']
                position = y['position']
                value_rank.append([player, calculate(expert_ranking, adp_ranking), position])
    elif player in only_in_adp:
        for x in crowds.json()['players']:
            if x['name'] == player:
                adp_ranking = x['adp']
                position = x['position']
                value_rank.append([player, calculate(0, adp_ranking), position])
    elif player in only_in_expert:
        for y in crowds.json()['players']:
            if y['name'] == player:
                expert_ranking = y['rank_ecr']
                position = y['player_position']                
                value_rank.append([player, calculate(expert_ranking, 0), position])
sorted_list = sorted(value_rank, key = lambda x: x[1])
panda_df = pd.DataFrame(sorted_list)
panda_df.index = panda_df.index + 1
panda_df.columns = ["Name", "Pick Value", "Position"]
print(panda_df)








