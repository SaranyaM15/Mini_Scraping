import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/best-of/fan-favorite-movies-shows-2022/ls566239698/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b5e51697-15f4-4e5c-8113-0673a342e617&pf_rd_r=FAYG4X9JF8ET2KQ855JX&pf_rd_s=center-10&pf_rd_t=60601&pf_rd_i=best-of&ref_=fea_csegbest_bo22_csegbest_fanrec22_hd"
r=requests.post(url)
html=r.content
#print(html)
s=BeautifulSoup(html,"html.parser")
#s=s.prettify()
#print(s)
a = s.find_all("h3",{"class":"lister-item-header"})
div=s.find_all("div",{"class":"inline-block ratings-imdb-rating"})
span=s.find_all("span",{"class":"lister-item-year text-muted unbold"})
p=s.find_all("p",{"class":"text-muted text-small"})
g=s.find_all("span",{"class":"genre"})
title=[]
year=[]
genre=[]
ratings=[]
flag=0
for i in a:
    for j in i.find_all("a"):
        title.append(j.text)
final_year=""
for Year in span:
    year.append(Year.text[1:5])
for s in p:
    for genre in g:
       genre.append(genre.text)
#print(genre)   
for k in div:
    ratings.append(k.text)
'''print(len(title))
print(len(ratings))
print(len(year))'''
print(len(genre))

'''import pandas as pd
data={"Movie_name":title,"Ratings":ratings,"year":year,"genre":genre}
df=pd.DataFrame(data)
file_name=pd.ExcelWriter("imdb_ratings.xlsx",engine="xlsxwriter")
df.to_excel(file_name,index=False)
file_name.save()'''


