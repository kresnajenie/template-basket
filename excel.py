from openpyxl import load_workbook  
import sys
import programTemplateBasket as sd
#import programTemplateBasket.py as tm

#def getData():
reload(sys)  
sys.setdefaultencoding('utf8')

filename = 'hasil-pertandingan.xlsx'

wb = load_workbook(filename)  
sheets = wb.get_sheet_names()  
worksheet = wb[sheets[1]]

done = False

reports=[]  
counter =0  
for i in tuple(worksheet.rows):  
	counter=counter+1
	strData=''
	for j in range(0,len(i)):
		s=i[j].value

		strData = strData +"|" + str(s).replace('\xc2\xa0','').replace('"','')
	#remove first delimiter
	strData = strData[1:]
	reports.append(strData)
	#print strData
	strItem = strData.split("|")
	team_home = strItem[2]
	team_away = strItem[6]
	score_home = strItem[3]
	score_away = strItem[5]
	print strItem[0], strItem[1], strItem[2], strItem[3], strItem[4], strItem[5], strItem[6]
	#sd.getMenuUtama(team_home, team_away, score_home, score_away)
	#sd.getMenuUtama(team_home, team_away, score_home, score_away)
	#sd.getMenuUtama(team_home, team_away, score_home, score_away)
	
	#print "Finished processing "  + str(counter) + " rows"  
	#print reports[3].replace("|", " ")
	#return strItem

	#+ args.harbour + " for "