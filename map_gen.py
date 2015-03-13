wall = '|'
flr = '.'
char = '@'

def map_proof():
	for row in range(7):
		for col in range(7):
			if col == 6 or (row == 0 and col == 6):
				print(wall, end='\n')
			elif (row == 0 or col == 0) or (row == 6):
				print(wall, end='')
			elif row == 3 and col == 3:
				print(char, end='')
			else:
				print(flr, end='')