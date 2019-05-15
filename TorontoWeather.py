from bs4 import BeautifulSoup as soup
import requests
global tempPanel
class Weather:
    myURL = 'https://weather.com/en-CA/weather/today/l/43.65,-79.38'
    pages = requests.get(myURL)
    contents = pages.content
    page = soup(contents, "lxml")
    span = page.findAll("span")
    tempPanel = page.find("div", {"class":"today_nowcard-section today_nowcard-condition"})

    def getTemperature(self):
        temp = self.tempPanel.find("div", {"class":"today_nowcard-temp"})
        span = temp.find("span")
        try:
            span.find("sup").decompose()#removes uneeded <sup> element
        except:
            print('')
        print('temperature is ' + span.text + ' degrees')
        return span.text

    def getFeelsLike(self):
        feelsPanel = self.page.find("div", {"class":"today_nowcard-feels"})
        feelslike = feelsPanel.find("span", {"class":"deg-feels"})
        try:
            feelslike.find("sup").decompose()
        except:
            print('')
        print('feels like ' + feelslike.text + ' degrees')
        return feelslike.text
