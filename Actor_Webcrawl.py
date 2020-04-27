from bs4 import BeautifulSoup
import requests, xlsxwriter

res = requests.get("https://www.imdb.com/list/ls025929404/")
soup = BeautifulSoup(res.text, 'html.parser')

wb = xlsxwriter.Workbook("Actors_Data.xlsx")
sheet = wb.add_worksheet("Actors")
sheet.write("A1","Names")
sheet.write("B1","Image_Link")
sheet.write("C1","Pesonality")
i=2

containers = soup.findAll("div",{"class":"lister-item mode-detail"})
for container in containers:
    ima = container.div.a.img["src"]
    image = ima
    sheet.write("B" + str(i),image)

    item = container.find("div",{"class":"lister-item-content"})
    name = item.h3.a.text
    sheet.write("A" + str(i),name)

    p_tags = container.findAll("p")
    bio = p_tags[1].text
    per = bio.split(sep=".")
    person = per[0]
    sheet.write("C" + str(i),person)

    i += 1

wb.close()
