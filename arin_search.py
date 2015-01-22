import re
import requests
from bs4 import BeautifulSoup

ip = raw_input('Enter an IP: ')

arin_html = requests.get('http://whois.arin.net/rest/ip/{ip_addr}'.format(ip_addr=ip))

arin_soup = BeautifulSoup(arin_html.content)
if arin_html.status_code == 200:
    c_name = arin_soup.find_all('name')
    p = re.compile(ur'(<name>)(.*)(</name>)')
    c_name = re.findall(p, str(c_name[0]))

    print ('\n' + str(c_name[0][1]))
    print arin_soup.startaddress.get_text() + '/' + arin_soup.cidrlength.get_text() + \
        ' - ' + arin_soup.endaddress.get_text()
    print '\nResults from: http://whois.arin.net/rest/ip/{ip_addr}'.format(ip_addr=ip)
else:
    print ('Error connecting to whois.arin.net')
    
