import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

pageNumber = 1
myList =[]

while (pageNumber < 30) :
    if (pageNumber == 1) : 
        URL = "https://englishjobs.pl/in/gdansk?q=python"
    else :
        URL = "https://englishjobs.pl/in/gdansk?q=python&page=" + str(pageNumber)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.findAll(class_="row job js-job")

    for job in results :

        position = job.find(class_="title").text.strip()
        content = job.find('p').text.replace('\n', '')

        if ('Python' in position) :
            link = 'https://englishjobs.es/' + job.find('a', class_="js-joblink joblink js-external")["href"]
            company = job.find('li').text
            

            publish = job.find('li').next_sibling.next_sibling.next_sibling.next_sibling.text
            publish = '2023 ' + publish
            publishingDate = date_object = datetime.strptime(publish, "%Y %B %d")

            if publishingDate > (datetime.now() - timedelta(days=120)) :

                print(company)
                if company not in myList :
                    myList.append(company)
                #print(position)
                #print(link)
                #print(company)
                #print(content.strip())
                #print(publishingDate)
                #print('--------------------------------------------------')
                #print('\n')

            '''
                with open('scraping.txt', 'a') as f:
                    f.write('------------- Barcelona --------------------------' +'\n')
                    //f.write(position +'\n')
                    //f.write(link +'\n')
                    f.write(company +'\n')
                    //f.write(content.strip() +'\n')
                    //f.write(str(publishingDate) +'\n')
                    //f.write('--------------------------------------------------' +'\n')
            '''
            
    pageNumber += 1

with open('scraping.txt', 'a') as f:
    f.write('------------------- Gdansk --------------------------' +'\n')
    for element in myList :
        f.write(element+'\n')