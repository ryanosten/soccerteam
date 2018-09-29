import csv

if __name__ == "__main__":
	with open("soccer_players.csv") as csvfile:
		num_teams = 3

		#read the csv store the contents of the csv in memory
		data = csv.DictReader(csvfile, delimiter=",")
		players = tuple(data)

		#count the number of experience attributes per team
		exp_count_yes = 0
		for row in players:
			if row['Soccer Experience'] == 'YES':
				exp_count_yes += 1

		#identify how many experienced players to put on each team
		exp_per_team = exp_count_yes/num_teams
		players_per_team = len(players)/num_teams

		#create a list of experienced players and non-experienced players
		exp_players = []
		non_exp_players = []

		for player in players:
			if player['Soccer Experience'] == 'YES':
				exp_players.append(player)
			else:
				non_exp_players.append(player)

		#assign players to each team
		sharks = []
		dragons = []
		raptors = []

		def assign_players():
			for player in exp_players:
				if (exp_players.index(player) + 4) % num_teams == 2:
					sharks.append(player)
				elif (exp_players.index(player) + 4) % num_teams == 1:
					dragons.append(player)
				elif (exp_players.index(player) + 4) % num_teams == 0:
					raptors.append(player)
			for player in non_exp_players:
				if (non_exp_players.index(player) + 4) % num_teams == 2:
					sharks.append(player)
				elif (non_exp_players.index(player) + 4) % num_teams == 1:
					dragons.append(player)
				elif (non_exp_players.index(player) + 4) % num_teams == 0:
					raptors.append(player)

		#write the teams to a file
		def write_team(team, players):
			with open("teams.txt", "a") as file:
				file.write('\n' + team + '\n')
				file.write('=============' + '\n')
				for player in players:
					file.write(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n')

		#write the welcome letters
		def welcome_letter(team, players):
			for player in players:
				player_ = player['Name'].lower().replace(" ", "_")
				
				letter = 'Dear ' + player['Guardian Name(s)'] + ',\n\n' 'We are writing to inform you that little ' + player['Name'] + ' is on the \n' + team + ' this year. The first practice with be Monday, June 1 at 12:00pm. \n\n' + 'Yours Truly, \n' + 'Dr. Claw'

				with open(player_ + '.txt', 'a') as file:
					file.write(letter)

	assign_players()
	write_team('Sharks', sharks)
	write_team('Dragons', dragons)
	write_team('Raptors', raptors)
	welcome_letter('Sharks', sharks)
	welcome_letter('Dragons', dragons)
	welcome_letter('Raptors', raptors)