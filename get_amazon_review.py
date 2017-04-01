from bs4 import BeautifulSoup
import urllib

year2017=0
year2016=0
year2015=0
year2014=0
year2013=0
year2012=0

for num in range(0,54):
    url1 = "https://www.amazon.com/iRobot-Roomba-Robotic-Vacuum-Cleaner/product-reviews/B013E9L4ZS/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber="
    url2 = str(num+1)
    url = url1 + url2
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all(attrs={"data-hook": "review-date"})
    while len(result)==0:
        response = urllib.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all(attrs={"data-hook": "review-date"})

    for i in range(0,len(result)):
        year=result[i].get_text().split(", ")[1]
        if year=="2017":
            year2017+=1
        elif year=="2016":
            year2016+=1
        elif year=="2015":
            year2015+=1
        elif year=="2014":
            year2014+=1
        elif year=="2013":
            year2013+=1
        else:
            year2012+=1

print("2017: "+str(year2017))
print("2016: "+str(year2016))
print("2015: "+str(year2015))
print("2014: "+str(year2014))
print("2013: "+str(year2013))
print("2012: "+str(year2012))
