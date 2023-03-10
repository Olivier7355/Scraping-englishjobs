# https://www.codeur.com/projects/371622-creation-d-une-base-de-donnee-de-contact

import requests
from bs4 import BeautifulSoup
import time


URL='https://www.societe.com/cgi-bin/liste-doc?champs=573%20entreprise%20dans%20le%20nord&ori=doc'

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}
req = session.get(URL, headers=headers)
result = BeautifulSoup(req.text, 'html.parser')
#print(result)


bloc = result.findAll(class_="ResultBloc bloclist doc")

for counter in range(20) :
    link = bloc[counter].find('a', class_="ResultBloc__link__content")['href']

    link = link.replace('/documents-officiels/', 'https://www.societe.com/societe/')
    link = link.replace('#statutshop', '')

    #print(link)
    time.sleep(3)

    URL = link
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
            'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
            'Accept':'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/webp,*/*;q=0.8'}
    req = session.get(URL, headers=headers)
    result = BeautifulSoup(req.text, 'html.parser')

    nomSociete = result.find('h1',class_="nomSociete").text.strip()
    adresseSociete = result.find('p',class_="etabDetails")
    adresse = adresseSociete.find(class_="ft-bold").text.strip()
    " ".join(adresse.split())

    raisonSocial = result.find(class_="FicheDonnees__donneeGenerique ml-6").text.strip()

    print('Nom : ', nomSociete)
    print('adressse : ', adresse)
    print('Raison sociate : ',raisonSocial)
    print('--------------------------------------------------------------------------')

