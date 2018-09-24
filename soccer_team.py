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

		#assign players to each team

		#write the teams to a file
		def write_team(team, players):
			with open("teams.txt", "a") as file:
				file.write('\nteam\n')
				file.write('=============')

	write_team('Sharks', players)
	write_team('Dragons', players)
	write_team('Raptors', players)