import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

pageNumber = 1

while (pageNumber < 2) :
    if (pageNumber == 1) : 
        URL = "https://englishjobs.es/in/barcelona?q=python"
    else :
        URL = "https://englishjobs.es/in/barcelona?q=python&page=" + str(pageNumber)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.findAll(class_="row job js-job")

    for job in results :

        position = job.find(class_="title").text.strip()
        if 'Python' in position :
            link = 'https://englishjobs.es/' + job.find('a', class_="js-joblink joblink js-external")["href"]
            company = job.find('li').text
            content = job.find('p').text.replace('\n', '')

            publish = job.find('li').next_sibling.next_sibling.next_sibling.next_sibling.text
            publish = '2023 ' + publish
            publishingDate = date_object = datetime.strptime(publish, "%Y %B %d")

            if publishingDate > (datetime.now() - timedelta(days=7)) :

                print(position)
                print(link)
                print(company)
                print(content.strip())
                print(publishingDate)
                print('--------------------------------------------------')
            
    pageNumber += 1