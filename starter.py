import json
import sys

with open('ipl_cricsheet/335982.json', 'r') as json_file:
    dicti = json.load(json_file)
batters = {}
bowlers = {}

for inn in dicti['innings']:
    for over in inn['overs']:
        for dlv in over['deliveries']:
            # Add player if not encountered yet
            if dlv['batter'] not in batters:
                batters[dlv['batter']] = {'runs':0, 'balls':0}
            if dlv['bowler'] not in bowlers:
                bowlers[dlv['bowler']] = {'runs':0, 'balls':0}

            # Calculate balls added to batter and bowler for this delivery
            if 'extras' not in dlv or ('wides' not in dlv['extras'] and 'no ball' not in dlv['extras']):
                batters[dlv['batter']]['balls'] += 1
                bowlers[dlv['bowler']]['balls'] += 1
            # Calculate runs added to batter and bowler for this delivery
            batters[dlv['batter']]['runs'] += dlv['runs']['batter']
            bowlers[dlv['bowler']]['runs'] += dlv['runs']['batter']

            if 'extras' in dlv and 'byes' not in dlv['extras'] and 'legbyes' not in dlv['extras']:
                bowlers[dlv['bowler']]['runs'] += dlv['runs']['extras']
                                
#print(batters)
#print(bowlers)

for bat in batters:
    print(bat + ': ' + str(batters[bat]['runs']) + '(' + str(batters[bat]['balls']) + ')')
for bowl in bowlers:
    print(bowl + ': ' + str(round(bowlers[bowl]['runs'] * 6 / bowlers[bowl]['balls'], 2)))
