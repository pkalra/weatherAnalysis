################# writing the loop for getting historical weather
import datetime
import urllib3
import json
import xlsxwriter as xw

http = urllib3.PoolManager()
key='fd27706e9098d47d'

tempm = list()
tempi = list()
precipm = list()
precipi = list()
fog = list()
icon = list()
rain = list()
snow = list()
hail = list()
thunder = list()
tornado = list()
write_to_excel = list()
date = list()
metro = list()

metro_list = ['GA/Atlanta','MA/Boston','IL/Chicago','TX/Dallas','CO/Denver','NV/Las_Vegas','CA/Los_Angeles','FL/Miami','NY/New_York','PA/Philadelphia','CA/San_Francisco','WA/Seattle']
for item in metro_list:
	tmp_metro = item
	start_date = datetime.date(2012, 1, 1)
	end_date = datetime.date(2014, 11, 30)
	delta = datetime.timedelta(days=1)
	d = start_date
	while d <= end_date:
		tmp_date = d.strftime('%Y%m%d')
		hist_r=http.request('GET', 'http://api.wunderground.com/api/'+ key +'/history_'+tmp_date+'/q/'+tmp_metro+'.json')
		hist_json_string=hist_r.data.decode('utf8')
		hist_parsed_json=json.loads(hist_json_string)
		a=hist_parsed_json['history']['observations']
		for item in a:
			if item['date']['hour'] == '19':
				metro.append(tmp_metro)
				date.append(d.strftime("%Y-%m-%d"))
				tempm.append(item['tempm'])
				tempi.append(item['tempi'])
				precipm.append(item['precipm'])
				precipi.append(item['precipi'])
				fog.append(item['fog'])
				rain.append(item['rain'])
				snow.append(item['snow'])
				hail.append(item['hail'])
				thunder.append(item['thunder'])
				tornado.append(item['tornado'])
				icon.append(item['icon'])
				break # some days have weather reported every 20 mins for same hour. Added break to take only first instance of hour 19
		d += delta

output_file = xw.Workbook("output.xlsx")
output_sheet1 = output_file.add_worksheet("output")  
header = list()
header.append("State/Metro")
header.append("Date")
header.append("Tempm")
header.append("Tempi")
header.append("Precipm")
header.append("Precipi")
header.append("Fog")
header.append("Rain")
header.append("Snow")
header.append("Hail")
header.append("Thunder")
header.append("Tornado")
header.append("Icon")
output_sheet1.write_row("A1", header)  
output_sheet1.write_column('A2', metro)
output_sheet1.write_column('B2', date)
output_sheet1.write_column('C2', tempm)
output_sheet1.write_column('D2', tempi)
output_sheet1.write_column('E2', precipm)
output_sheet1.write_column('F2', precipi)
output_sheet1.write_column('G2', fog)
output_sheet1.write_column('H2', rain)
output_sheet1.write_column('I2', snow)
output_sheet1.write_column('J2', hail)
output_sheet1.write_column('K2', thunder)
output_sheet1.write_column('L2', tornado)  
output_sheet1.write_column('M2', icon)  
output_file.close()



########################### TOP 15 metros
Atlanta                   GA
Boston                    MA
Chicago                   IL / Chicago Midway/ Chicago Meigs/ 
Dallas/Ft Worth           TX ; use only Dallas in url
Denver                    CO
Las Vegas                 NV / North Las Vegas
Los Angeles		  CA
Miami                     FL
New York                  NY / New York JFK
Philadelphia              PA
San Francisco             CA
Seattle                   WA / Seattle Boeing
Toronto                   ON   ; country - CA
London Weather Center        UK  / London City

