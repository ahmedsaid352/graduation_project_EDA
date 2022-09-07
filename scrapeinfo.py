from cgitb import html
from bs4 import BeautifulSoup
import pandas as pd

with open('html2.txt', 'r') as file:
    html = file.read().replace('\n', '')

soup = BeautifulSoup(html, 'html.parser')

plant_name = []
n_of_imgs =[]

names_elements = soup.select('#site-content > div.sc-iJTIzp.dEsnHS > div.sc-dGHKFW.cpYUJD > div.sc-dCkZnI.ceoMyZ > div.sc-hZaSAO.iVwyYi > div > div.sc-eHAsqE.ginGnF > div > div.sc-gcFSfr.gquipn > div.sc-dTbhCw.eeugBO > div > div.sc-IAann.fLFzeF > p')
files_elements = soup.select('#site-content > div.sc-iJTIzp.dEsnHS > div.sc-dGHKFW.cpYUJD > div.sc-dCkZnI.ceoMyZ > div.sc-hZaSAO.iVwyYi > div > div.sc-eHAsqE.ginGnF > div > div.sc-gcFSfr.gquipn > div.sc-dTbhCw.eeugBO > div > div.sc-IAann.fLFzeF > span')
for i in range(len(names_elements)):
    plant_name.append(names_elements[i].text)
    n_of_imgs.append(files_elements[i].text)

information = {
    'plant name':plant_name,
    'number of images':n_of_imgs,
}
df = pd.DataFrame(information)
df.to_excel('datasetinfo2.xlsx',index=False)

