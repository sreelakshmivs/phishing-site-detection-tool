# Python program to scrape website
# and save quotes from website
import re
from bs4 import BeautifulSoup as BS

import requests
from bs4 import BeautifulSoup
#import csv.
from urlparse import urlparse

def func(URL):
    #http://onceambientstore.com/fotos/82c27bced2f6ac2f...
    #URL = "http://www.iiitmk.ac.in"
    #URL = "http://www.facebook.com"
    #URL = "http://www.aimele.com/dopbox/db/view/"#not phish
    #URL = "http://merkavapro.online/ssh/sfa7-110"#phished

    #URL = "http://merkavapro.online/ssh/sfa7-110"#phished
    #URL = "http://merkavapro.online/ssh/sfa7-110"#phished
    #URL = "https://alkamal.org.au/data/qoqdoc"#phished
    #URL = "http://bit.ly/18L6WO"
    #URL ="http://merkavapro.online/ssh/sfa7-110"
    #http: // hossei7n.000webhostapp.com / App % 20insta / App % ...
    row = requests.get(URL)

    soup = BeautifulSoup(row.content, 'html.parser')

    hrefs = []  # a list to store hyperlinks

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        print(link.get('a'))


    '''for row in soup.find_all('form'):

        print(row.get('action'))
        len(row.get('action'))

        if len(row.get('action')) == 0:
            print("phished")
        else:
            print("not phished")'''

    print('Anchor\n----')


    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    print(links)

    siz = int(len(links))
    print('total = ', siz)
    bandflag = 0
    if(siz == 0):
        bandflag = 1
        print("phished")


    count = 0
    for i in range(siz):
        if (links[i] == '#') | ('js' in links[i]):
            count = count +1

    print('suspicious = ', count)
    percentageA = 0;
    if(siz > 0):
        percentageA = (count / siz) * 100
    print("Percentage")
    print(percentageA, '%')

    print('status of the given site\n------------------------')
    if(percentageA < 31):
        print("Legitimate")
    elif((percentageA >= 31) and (percentageA<= 67)):
        print("suspicious")
    else:
        print("phishing")



    print('meta\n----')
    metas = []
    countmeta = 0
    for meta in soup.find_all('meta'):
        metas.append(meta.get('meta'))
    print(metas)
    sizemeta = int(len(metas))
    print("Total = ", sizemeta)
    for i in range(sizemeta):
        if (links[i] == '#'):
            countmeta = countmeta + 1

    print('suspicious = ', countmeta)
    percentage = 0;
    if(percentage > 0):
        percentage = (countmeta / sizemeta) * 100
    print("Percentage")
    print(percentage, '%')

    print('status of the given site\n------------------------')
    if (percentage < 31):
        print("Legitimate")
    elif ((percentage >= 31) and (percentage <= 67)):
        print("suspicious")
    else:
        print("phishing")

    print('script\n------')



    scripts = []
    countscript = 0
    for script in soup.find_all('script'):
        scripts.append(script.get('href'))
    print(scripts)
    sizescript = int(len(scripts))
    print("Total = ", sizescript)
    for i in range(sizescript):
        if (scripts[i] == '#'):
            countscript= countscript + 1

    print('suspicious = ', countscript)
    percentage = 0;
    if(percentage>0):
        percentage = (countscript / sizescript) * 100
    print("Percentage")
    print(percentage, '%')

    print('status of the given site\n------------------------')
    if (percentage < 31):
        print("Legitimate")
    elif ((percentage >= 31) and (percentage <= 67)):
        print("suspicious")
    else:
        print("phishing")






    parsed_uri = urlparse(URL)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    print("DOMAIN NAME\n-----------")
    print(domain)
    '''num_of_domains = domain.split('http://')[1].split('/')[1]
    print(num_of_domains[0])'''

    print("SPLITED DOMAIN NAMES\n---------------------")
    for url in parsed_uri:
        spltAr = url.split(".")
        i = (0, 1)[len(spltAr) > 1]

        #dm = domain.split('http://')[1]
        dm = spltAr[i].split('http')[0].split('.')[0].split(':')[0].lower()
        print(dm)

    print("-----")
    if(dm == ' '):
            print("phished")
    else:
            print("legitimate")
    '''dmsize = int(len(dm))
    print(dmsize)
    
        #print(dm)
        #dmarray = []
        #dmarray = dm
        #print(dmarray)
    
    if (dmsize == 0):
    
        print("no domains,status = phished site")
    else:
        print("only one domain\nstatus = legitimate")'''





    '''html = '''
    '''<html><head></head>
    <body>
    <a href = "http://gerritsenautos.nl/boa_6/step3.php">My homepage</a>
    </body>
    </html>'''

    """soup1 = BeautifulSoup(html, 'html.parser')
    for a in soup1.find_all("a", text=re.compile("home")):
        anchor = a['href'].split()
        print("the len=", len(anchor))
        print("sdf")
        print(a['href'])"""
    '''for a in soup.findAll('a'):
        info = a.get('href')
    print(info)'''

    #for row in soup.find_all('a'):
        #print(row.get('href'))

    '''def extract_links(html):
      soup = BeautifulSoup(html)
      anchors = soup.findAll('a')
      print(anchors)
      links = []
      for a in anchors:
        links.append(a['href'])
      print(links)'''





    '''anchor = soup.findAll('a')
    print(anchor)'''

    '''links = []
    for a in anchor:
        if ('href') in a.attrs:
          links.append(a['href'])
    print(links)'''

    '''if anchor == " ":
        print("Phished")
    elif anchor == "#":
        print("phished")
    else:
        print("Not phished")'''

    '''metatags = []
    metatags[0] = soup.find_all('meta', attrs={'name':'keywords'})
    print(metatags[0])'''
    #for meta in metatags:
        #print(meta)


    '''for tag in soup.find_all("meta"):
        if tag.get("property", None) == "og:title":
            print(tag.get("content", None))
        elif tag.get("property", None) == "og:url":
            print(tag.get("content", None))'''
    '''for row in soup.find_all('meta'):
        print(row.get('href'))'''

    if((percentageA>31)or(dm==' ')):
        s = "TOTAL RESULT\n---------------\nPHISHED SITE DETECTED\n"
        return s
    if(bandflag == 1):
        s = "TOTAL RESULT\n---------------\nPHISHED SITE DETECTED\n"
        return s
    else:
        s = "TOTAL RESULT\n---------------\nSite is not Phished"
        return s

#func("http://www.cr-mufg-jp.mobi/RegistUser/cojp_head_my...")
