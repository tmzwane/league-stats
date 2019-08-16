import sys
import os
import re
import operator

# Ask user for a txt file name
file_name = input("Enter the name of the file with soccer results: \n")

file_path = os.path.join(os.path.curdir, file_name)

# Open and read file
file = open(file_path, "r")

league_array = []
teams = []
match_result = []
final_results = []

for results in file:
	# Strip and split each team to seperate arrays
	team_names = results.rstrip('\r\n').split(',')
	team_names[1].lstrip()

	# Get the scores from the arrays for the team
	teamA_score = re.findall(r'\d+', team_names[0])
	teamA_score = int(teamA_score[0])
	teamB_score = re.findall(r'\d+', team_names[1])
	teamB_score = int(teamB_score[0])

	match_result.append(team_names)

	# Get the names of the team and append to the teams list and build score card
	teamA_name = team_names[0].replace(str(teamA_score), '').lstrip().rstrip()
	teamB_name = team_names[1].replace(str(teamB_score), '').lstrip().rstrip()


	# Match Results Calculations
	if teamA_name not in teams:
		teams.append(teamA_name)
	if teamB_name not in teams:
		teams.append(teamB_name)

entry = 0
for team_name in teams:
	# Team data structures
	team_points_card = {
		"name": team_name,
		"won": 0,
		"draw": 0,
		"lost": 0,
		"points": 0
	}

	entry += 1

	# Go through each team and get the points and number of plays
	for results in match_result:
		
		results[1].lstrip()

		if team_name in results[0]:
			team_score = re.findall(r'\d+', results[0])
			team_score = int(team_score[0])
			other_team_score = re.findall(r'\d+', results[1])
			other_team_score = int(other_team_score[0])

			if team_score > other_team_score:
				team_points_card['won'] += 1
				team_points_card['points'] += 3
			elif team_score == other_team_score:
				team_points_card['draw'] += 1
				team_points_card['points'] += 1
			else:
				team_points_card['lost'] += 1

		elif team_name in results[1]:
			team_score = re.findall(r'\d+', results[1])
			team_score = int(team_score[0])
			other_team_score = re.findall(r'\d+', results[0])
			other_team_score = int(other_team_score[0])

			if team_score > other_team_score:
				team_points_card['won'] += 1
				team_points_card['points'] += 3
			elif team_score == other_team_score:
				team_points_card['draw'] += 1
				team_points_card['points'] += 1
			else:
				team_points_card['lost'] += 1

	final_results.insert(entry, team_points_card)

final_results.sort(key=operator.itemgetter('points'), reverse=True)

key = 0
for output in final_results:
	key +=1
	print(str(key) + '. ' + output['name'] + ', ' + str(output['points']) + ' pts')
	print()



