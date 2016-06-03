"""
This script is used to read and parse XML data into csv 

Data source: Nation Institute of Health(nih)
url: "http://exporter.nih.gov/ExPORTER_Catalog.aspx?sid=0&index=1"
	
Created on 06.03.2016  by Paul Sirma 
"""

#Packages for Notepad++
import os.path, sys
sys.path.append('C:/Anaconda2/Lib/site-packages/')


#packages need to run the program 
import urllib, urllib2 , pprint , zipfile , re, csv , os
from BeautifulSoup import *

#Define the path where the original XML data is saved 
path = "C:\Users\psirma\Desktop\Zipfile\original_data".replace("\\" , "/")  
path2 = "C:\Users\psirma\Desktop\Zipfile".replace("\\" , "/")  

diri = os.listdir(path)

for d in diri:
	
	file = zipfile.ZipFile(path + "/" +d, "r")   #loading the Zipfile
	
	#Opening a csv file to write the final output 
	outp = csv.writer(open(path2+'/_' + d + '.csv', 'wb'))
	
	#writting column titles 
	titles = ['Application_id' , 'Abstract']
	outp.writerow(titles)
	
	#Getting the file names in file
	file_name = ''
	for name in file.namelist():
		file_name = name
		
	print "************************"
	print 'I am reading file:' , d 
	
	# Opening the zip file 
	# Note: The file is too big. Read it in chunks and split it by tag = <row>	
	doc = file.open(file_name).read().split('<row>')

	for d in doc :
		#Parsing the XML file with BeautifulSoup
		soup = BeautifulSoup(d)
		
		#Store application_id & abstract_text
		application = soup('application_id')
		abs_text = soup('abstract_text' )
		
		#Cleaning application_id and abstract_text to remove the tags 
		app_id = ''
		app_text = ''
		for r in application:
			print "****"
			app_id =  r.text
		for t in abs_text:
			app_text = t.text
		#Removing tab spaces 
		app_text = re.sub(r'[\s+]', ' ', app_text)
		
		#Join application_id and abstract_text and write the data to outp
		row = [app_id , app_text]
		print "*********"
		print row 
		outp.writerow(row)
		
	
	#When we finish reading the file, exit 
	if not doc:
		print "No more file to read"
		exit()
	
print "****** The End **********"
	
	
	
	
	

	

	




