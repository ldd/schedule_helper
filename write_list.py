import csv										#to write to a csv file
from os import listdir							#to find html files
from use_list import decode_html, clean_stuff	#to decode and clean the html tables

'''
Write csv file (rows to output file)
'''
def write_help(rows, output_file):
	myfile = open(output_file, 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

	for i in range(len(rows)):
		wr.writerow(rows[i])
'''
write to path the information so far gathered, for days, 
ignoring the courses in ignore_list
'''
def write_schd_info(path, days,ignore_list):
	#find all html files in the current path
	files = listdir(path)
	html_files = [page for page in files if page.find('.html') != -1]

	table_array = []
	final_table = []
	
	#add as arrays all html files in current path
	for i in range(len(html_files)):
		input_file = html_files[i]
		table_array += decode_html(path + input_file)

	#clean this array, add the day [i] which we are saving
	for i in list(days):
		final_table += [i] + clean_stuff(table_array, 0, i, ignore_list)

	output_file = path + 'courses.csv'
	write_help(final_table, output_file)
	return final_table

''' MAIN PART '''
if ( __name__ == "__main__" ):
	my_path = '/home/ldd/Dropbox/McGill/stuff/'
	ignore_list = ['7','5','6','4','273','202','206','250','251']
	write_schd_info(my_path, 'MT',ignore_list)
''' END OF MAIN '''
