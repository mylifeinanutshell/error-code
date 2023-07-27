from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            tab_list=[]
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    tab_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tab_list.append(li_tag.conetent[0])
                    except:
                        tab_list.append("")
            planets_data.append(tab_list)
        browser.find_element(by=By.XPATH,values='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_1=pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planet_1.to_csv("scarpdata.cvs",index=True,index_label="id")
    


