from  bs4 import BeautifulSoup
import requests
from csv import writer

# Collect and parse first page
URL = "https://www.trustpilot.com/review/houseofmalt.co.uk?page="
with open('sentiment.csv', '+w', encoding= 'utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Review','Score']
    thewriter.writerow(header)
    for page in range(2,1400):
        page = requests.get(URL + str(page))
        soup = BeautifulSoup(page.content, 'html.parser')
        for sit in soup.find_all('div', class_ ="typography_typography__QgicV typography_bodysmall__irytL typography_weight-medium__UNMDK typography_fontstyle-normal__kHyN3 styles_consumerName__dP8Um"):
        #name
            name = sit.text
            print(name)
        for kit in soup.find_all('img', alt= {"Rated 5 out of 5 stars","Rated 4 out of 5 stars","Rated 3 out of 5 stars","Rated 2 out of 5 stars","Rated 1 out of 5 stars","Rated 0 out of 5 stars"}):
        #ratings
            content = kit
            print(content)
        for fit in soup.find_all('a', class_="link_internal__7XN06 typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV link_notUnderlined__szqki typography_color-inherit__TlgPO"):
         #title
            title = fit.text
            print(title)
        for hit in soup.find_all('p',class_="typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3"):
        # review
            review = hit.text
            info = [review, content]
            thewriter.writerow(info)
            print(review)





