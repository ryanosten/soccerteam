import csv

if __name__ == "__main__":
	with open("soccer_players.csv") as csvfile:
		#read the csv store the contents of the csv in memory
		data = csv.DictReader(csvfile, delimiter=",")
		players = tuple(data)

		#count the number of experience attributes per team
		exp_count = {'yes': 0, 'no':0}
		for row in players:
			if row['Soccer Experience'] == 'YES':
				exp_count['yes'] += 1
			else:
				exp_count['no'] += 1
		print(exp_count)
		#determine how many of each attr to put per team
		#split the team members into equal groups, with even experience attrs
		#write the groups to a file
		def createTeams(players, per_team):
			file = open("teams.txt", "a")
			file.write('some shit')

	createTeams('a', 3)