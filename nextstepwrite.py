import csv
from datetime import datetime
from os import listdir
from use_list import decode_html, clean_stuff

#Write csv file
def write_stuff(rows, output_file):
	myfile = open(output_file, 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

	for i in range(len(rows)):
		wr.writerow(rows[i])

def beauty(path, days,ignore_list):
	files = listdir(path)
	html_files = [page for page in files if page.find('.html') != -1]
	table_array = []
	final_table = []
	
	for i in range(len(html_files)):
		input_file = html_files[i]
		table_array += decode_html(path + input_file)

	for i in list(days):
		final_table += [i] + clean_stuff(table_array, 0, i, ignore_list)

	output_file = path + 'courses.csv'
	write_stuff(final_table, output_file)
	return final_table

def pac(pp):	
	start_time = []
	end_time = []

	try:
		for i in range(1,(len(pp)-1)):
			start_time.append(pp[i][0])
			end_time.append(pp[i][1])
		
	except:
		pass

''' MAIN PART '''
if ( __name__ == "__main__" ):
	my_path = '/home/ldd/Dropbox/McGill/stuff/'
	ignore_list = ['7','5','6','4','273','202','206','250']
	pp = beauty(my_path, 'MT',ignore_list)
	
''' END OF MAIN '''
