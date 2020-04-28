# Objective: Use the BeautifulSoup and requests Python packages read a table and write it to file

import requests, pandas as pd
from bs4 import BeautifulSoup as soup

url = 'https://www.worldometers.info/world-population/population-by-country/'
r = requests.get(url)
r_html = r.text

parsed_data = soup(r_html, features="lxml")
country_data = parsed_data.find_all('table')[0]
df = pd.read_html(str(country_data))[0]
print(country_data)

# create a function to read all data from the table

def getCountryData(a,b,c,d,e,f,g,h,i,j,k):
    data = pd.DataFrame(
        {
            'a': df[a],
            'b': df[b],
            'c': df[c],
            'd': df[d],
            'e': df[e],
            'f': df[f],
            'g': df[g],
            'h': df[h],
            'i': df[i],
            'j': df[j],
            'k': df[k]
        }
    )
    return data

# call the function
cntry_data = getCountryData('Country (or dependency)','Population (2020)','Yearly Change','Net Change','Density (P/Km²)',
                            'Land Area (Km²)','Migrants (net)','Fert. Rate','Med. Age','Urban Pop %','World Share')
cntry_data.columns = ['Country (or dependency)','Population (2020)','Yearly Change','Net Change','Density (P/Km²)',
                            'Land Area (Km²)','Migrants (net)','Fert. Rate','Med. Age','Urban Pop %','World Share'
                      ]
export_to_csv = cntry_data.to_csv(r'C:\Users\Ashoo\Documents\PythonPlayground\learnpy\data\country_population_data.csv',
                                  index= None, header= True)

