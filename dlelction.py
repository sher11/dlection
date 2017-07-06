#
# @author Salim Mahammad Almas
#
from bs4 import BeautifulSoup
import urllib2

LINK = "http://eci.nic.in/eci_main1/statistical_reportge2014.aspx"
PDF = []
XLSX = []


def get_html(url):
    return urllib2.urlopen(url).read()


html = get_html(LINK)
lux_soap = BeautifulSoup(html, "html.parser")

for link in lux_soap.find_all('a'):
    url = link["href"]
    if str(url).endswith(".pdf"):
        PDF.append(url)
    elif str(url).endswith(".xlsx"):
        XLSX.append(url)


def get_title(link):
    quoted = str(link).split("/")[str(link).split("/").__len__() - 1]
    while quoted.__contains__("%20"):
        quoted = quoted.replace("%20", " ")

    return quoted


def download(list, path):
    for link in list:
        link = urllib2.quote(link, safe="%/:=&?~#+!$,;'@()*[]")
        print link
        contents = urllib2.urlopen(link).read()
        tittle = get_title(link)
        pure_path = path + "/" + tittle
        file = open(pure_path, 'w+')
        file.write(contents)
        file.close()


download(PDF, "data/pdf")
download(XLSX, "data/xlsx")

print "Completed"
