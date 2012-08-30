from BeautifulSoup import BeautifulSoup	#to get the table info as an array
from datetime import datetime			#to sort/manipulate the times

'''
decode 
'''
def decode_html(input_file):
	all_rows = []
	try:
		soup = BeautifulSoup(open(input_file))
		course_table = soup.find('table','datadisplaytable')
		all_rows = course_table.findAll('tr')
	except:
		exit(1)
		
	#get titles of the table
	titles = []
	for i in all_rows[1]:
		titles.append([])
		try:
			#3 options: either the tr contains an acronym, an abbr or plain text
			#we append this to an array
			if (i.string and len(i.string)>1):
				titles[0].append(i.string.strip().encode('utf-8'))
			if i.abbr.string:
				titles[0].append(i.abbr.string.strip().encode('utf-8'))
			if i.acronym.string:
				titles[0].append(i.acronym.string.strip().encode('utf-8'))
		except:
			pass #do nothing and keep on going

	#get the rest of the table
	k=1
	for i in all_rows:
		titles.append([])
		for j in i.findAll('td','dddefault'):
			try:
				if (j.string and len(j.string)>=1):
					titles[k].append(j.string.strip().encode('utf-8'))
			except:
				pass
		k= k+1
		
	return titles

'''clean the rows array. 
Options:
	print_tables: 	1 print tables, 0 don't
	day: 			day of the week to be considered
	ignore_list:	courses to ignore (as a list)
'''
def clean_stuff(rows, print_tables, day, ignore_list):
	day_data = []
	for i in range((len(rows))):
		try:

			if ('&nbsp;' == rows[i][0]):
				rows[i].pop(0)
				if (len(rows[i][0]) != 4):
					rows[i] = ''


			if ('Lecture' != rows[i][3] and 'Sec' != rows[i][3]):
				rows[i] = ''
			
			#prepare to delete those rows that have courses in the ignored_list
			for rule in ignore_list:
				if (rows[i][1].find(rule,0,len(rule)) != -1):
					rows[i] = ''
	
			#add to the day data:
			# the starting time dates[0], 
			#		ending time date[1],
			#		course subj rows[i][0],
			#	  course number rows[i][1],
			#course description rows[i][5],
			if (rows[i][6].find(day) != -1):
				dates = rows[i][7].split('-')
				dates[0] = datetime.strptime(dates[0], '%I:%M %p')
				dates[1] = datetime.strptime(dates[1], '%I:%M %p')
				dates.append(rows[i][0])
				dates.append(rows[i][1])
				dates.append(rows[i][5])
				day_data.append(dates)
			
			#prepare to delete cancelled courses
			if ('Cancelled' == rows[i][-1]):
				rows[i] = ''
		except:
			pass

	ret = []

	try:
		#delete the rows prepared for deletion, 
		rows = filter(len, rows)
		
		#tl;dr: in the titles, one column header is there to check the course
		#for the checklist.
		#we drop it because we dont need it
		rows[0].pop(0)		
		
		#sort data in reverse order according to date
		day_data.sort(reverse=True)

	except:
		print 'Error reading data from html files. Are they valid?'

	#append row information if print_tables is true
	if (print_tables == True):
		for i in range(len(rows)):
			ret.append(rows[i])

	#append the day data information
	for i in range(len(day_data)):
		ret.append(day_data[i])
	return ret


''' MAIN PART '''
if ( __name__ == "__main__" ):
	pass
''' END OF MAIN '''
