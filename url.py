import csv
import requests 
import shutil
from bs4 import BeautifulSoup
extension=".png"

with open('path to CSV file') as csv_file:
    csv = csv.reader(csv_file, delimiter=',')
    
    next(csv, None)
    for row in csv:
        
        page=requests.get(row[0])
        #print(row[0])
        page_txt=BeautifulSoup(page.text,'html.parser')
        s=page_txt.find_all(id="firstHeading")
        t=str(s[0]).split('>')
        q=str(t[1]).split(" (")
        #print(q[0])
        ss=page_txt.find_all('img')
        tt=str(ss[2]).split('src="')
        qq=str(tt[1]).split('"')
        #print(qq[0])
        filename = str(qq[0]).split("/")[-1]
        r = requests.get(qq[0], stream = True)
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)