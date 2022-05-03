import csv, getpass

if __name__ == '__main__':
	correct = 'n'

	# Get filename details
	while correct == 'n' or correct == 'N':
		date = input('Event date [YYYY-MM-DD]: ')
		event = input('Event name: ')

		correct = input(date + '_' + event + ' - Correct [y/n]: ')
		print('\n')

	filename = date + '_' + event + '.csv'
	
	# Get length of file if it exists.
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			length = len(list(reader))
	except:
		length = 0
	
	# Write routine
	with open(filename, 'a') as f:

		writer = csv.writer(
			f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		
		# Only write header to a new file
		if length == 0:
			writer.writerow(['id', 'lastname', 'firstname'])

		swipe = None
		count = 0

		# Accept user swipes and write to specified file.
		while(swipe != 'quit'):
			
			swipe = getpass.getpass(prompt='Please swipe your FSU Card:')
			
			# Valid read
			if len(swipe) > 2 and swipe[1] == 'B':
				id = swipe[10:18]
				name = swipe.split('^')
				lastname = name[1].split('/')[0]
				firstname = name[1].split('/')[1].rstrip()
				
				count += 1
				writer.writerow([id, lastname, firstname])
				print('Thanks for checking in ' + firstname+ '!\n')				
			# Invalid read
			elif swipe != 'quit':
				print('READ ERROR : PLEASE RESWIPE\n')
			# Display checkin data on exit
			else:
				print('\n*****Quitting Tracker*****\nCHECKED IN:', count, '\n')		
