import csv, getpass

if __name__ == '__main__':
	correct = 'n'
	loop = True

	while correct == 'n' or correct == 'N':
		date = input('Event date [YYYY-MM-DD]: ')
		event = input('Event name: ')

		correct = input(date + '_' + event + ' - Correct [y/n]: ')
		print('\n')

	filename = date + '_' + event + '.csv'
	with open(filename, "w") as f:
		

		writer = csv.writer(
			f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['id', 'lastname', 'firstname'])

		swipe = None
		count = 0
		while(swipe != 'quit'):
			
			swipe = getpass.getpass(prompt='Please swipe your FSU Card:')
			
			if len(swipe) > 2 and swipe[1] == 'B':
				id = swipe[10:18]
				name = swipe.split('^')
				lastname = name[1].split('/')[0]
				firstname = name[1].split('/')[1]
				
				count += 1
				writer.writerow([id, lastname, firstname])
				print('Thanks for checking in ' + firstname+ '!\n')				
			elif swipe != 'quit':
				print('READ ERROR : PLEASE RESWIPE\n')

		print('\nChecked in:', count)
