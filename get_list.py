#!/usr/bin/python
import urllib, urllib2, cookielib    #to get url
import getpass                       #to hide password (just to pretend to be secure)
'''
fetch the html page containing the master table 
for the 'subject'/'faculty' in question.
Saves to 'path'
'''
def fetch_list(subject,faculty,path):
	username = raw_input("Please enter your username(ex:john.smith@mail.mcgill.ca)\n")
	password = getpass.getpass(
	"Please enter your password\n[Press enter when done. HIDDEN FOR YOUR PROTECTION]\n")

	try:
		#login to McGill
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		login_data = urllib.urlencode({'sid' : username, 'PIN' : password})
		opener.open('https://banweb.mcgill.ca/pban1/twbkwbis.P_ValLogin')
		opener.open('https://banweb.mcgill.ca/pban1/twbkwbis.P_ValLogin', login_data)

		#get the table
		#note: why is this data so ugly? Pretty methods don't work. *sighs*
		data = ('term_in=201209&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy' +
		'&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_subj='+subject +
		'&sel_coll=' + faculty + '&sel_crse=%25&sel_title=%25&sel_schd=%25&sel_from_cred=0&sel_to_cred=99'+
		'&sel_levl=%25&sel_ptrm=%25&sel_instr=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a')

		gpaStuff = opener.open('https://banweb.mcgill.ca/pban1/bwskfcls.P_GetCrse', data)
		gpaHtml = gpaStuff.read()
		
		#write the table to a file
		title = path + "%s_list.html" % subject
		myFile = open(title, 'w+')
		myFile.write(gpaHtml)
		myFile.close()

	except:
		print 'error'
'''end of fetch_list'''

''' MAIN PART '''
if ( __name__ == "__main__" ):
	#sample test performed when not called by scheduler_helper
	subj = 'COMP'
	fac = 'SC'
	my_path = '/home/ldd/Dropbox/McGill/stuff/'
	fetch_list(subj, fac,my_path)
''' END OF MAIN '''
